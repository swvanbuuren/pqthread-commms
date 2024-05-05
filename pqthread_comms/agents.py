"""
Thread communicator module for sending and receiving information from one thread
to another using a sender and receiver
"""

from copy import copy
from contextlib import contextmanager
from pqthread_comms.qt import QtCore
from pqthread_comms import utils


class RootTCException(Exception):
    """ Root Exception of the threads module """


class WorkerAgentException(RootTCException):
    """ This Exception is raised if no signal was sent to a slot and thus no
    message was received"""


class GUIAgentException(RootTCException):
    """ This Exception is raised if an error at receiver side was detected """


class WorkerAgent(QtCore.QObject):
    """ Enables exchange of data with GUIAgent using signal/slots """
    createSignal = QtCore.Signal(list, dict)
    modifySignal = QtCore.Signal(int, dict)
    requestSignal = QtCore.Signal(int, list)
    methodSignal = QtCore.Signal(int, str, list, dict)
    deleteSignal = QtCore.Signal(int)
    dataRecevied = QtCore.Signal()

    def __init__(self, name, parent=None):
        super().__init__(parent)
        self.no_message = object()
        self.error = False
        self.message = self.no_message
        self.name = name

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name})'

    def connect_agent(self, gui_agent):
        """ Connects the sender to a gui_agent """
        gui_agent.signal.connect(self.slot)
        gui_agent.error.connect(self.error_detected)
        self.createSignal.connect(gui_agent.create_slot)
        self.modifySignal.connect(gui_agent.modify_slot)
        self.requestSignal.connect(gui_agent.request_slot)
        self.methodSignal.connect(gui_agent.method_slot)
        self.deleteSignal.connect(gui_agent.delete_slot)

    def create(self, *args, **kwargs):
        """ Send out a signal and obtain data from gui_agent"""
        with utils.wait_signal(self.dataRecevied):
            self.createSignal.emit(args, kwargs)
        return self.read_message()

    def modify(self, index, **kwargs):
        """ Send out a one-way signal with given arguments and keyword arguments """
        self.modifySignal.emit(index, kwargs)

    def request(self, index, *args):
        """ Obtain data from gui_agent"""
        with utils.wait_signal(self.dataRecevied):
            self.requestSignal.emit(index, args)
        return self.read_message()

    def method(self, index, func_name, *args, **kwargs):
        """ Send out a signal to execute a method on the gui_agent class """
        with utils.wait_signal(self.dataRecevied):
            self.methodSignal.emit(index, func_name, args, kwargs)
        return self.read_message()

    def delete(self, index):
        """ Send out a signal to delete object at index on the gui_agent class """
        self.deleteSignal.emit(index)

    def read_message(self):
        """ Helper method, that reads message set by slot and returns a copy """
        if self.message is self.no_message:
            if self.error:
                return self.message
                # we don't raise this error anymore, since it's caught in the
                # GUIAgency
                # raise GUIAgentException('Error detected at gui_agent side')
            if not self.error:
                raise WorkerAgentException('No message received')
        message = copy(self.message)
        self.message = self.no_message
        return message

    @QtCore.Slot(object)
    def slot(self, data):
        """ Slot for receiving data """
        self.message = data
        self.dataRecevied.emit()

    def error_detected(self):
        """ If a gui_agent error is detected ... """
        self.error = True


class GUIAgent(QtCore.QObject):
    """ A receiver for operations whose instructions were sent by WorkerAgent """
    signal = QtCore.Signal(object)
    error = QtCore.Signal()

    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller = controller
        self.create = controller.create
        self.modify =  controller.modify
        self.request = controller.request
        self.method = controller.method
        self.delete = controller.delete

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name})'

    @contextmanager
    def register_exception(self):
        """ Shorthand to register errors at receiver side """
        try:
            yield
        except BaseException:
            self.error.emit()
            raise

    @QtCore.Slot(list, dict)
    def create_slot(self, args, kwargs):
        """ Slot for creating a new class instance """
        with self.register_exception():
            val = self.create(args, kwargs)
            self.signal.emit(val)

    @QtCore.Slot(int, dict)
    def modify_slot(self, index, kwargs):
        """ Slot for modifying an instance attribute """
        self.modify(index, kwargs)

    @QtCore.Slot(int, list)
    def request_slot(self, index, args):
        """ Slot for requesting an instance attribute """
        with self.register_exception():
            self.signal.emit(self.request(index, args))

    @QtCore.Slot(int, str, list, dict)
    def method_slot(self, index, func, args, kwargs):
        """ Slot for calling a class instance method """
        with self.register_exception():
            self.signal.emit(self.method(index, func, args, kwargs))

    @QtCore.Slot(int)
    def delete_slot(self, index):
        """ Slot for closing/deleting a class instance object at index """
        with self.register_exception():
            self.delete(index)
