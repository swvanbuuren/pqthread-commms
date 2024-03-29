"""
Module for controlling of and communication between worker and GUI thread. It
provides a base class for controllers that control the communication between a
worker thread and the GUI thread.
"""

import sys
try:
    from PySide6 import QtCore, QtWidgets
except ImportError:
    from PySide2 import QtCore, QtWidgets
from pqthread_comms import agents
from pqthread_comms import descriptors


class WorkerAgency(QtCore.QObject):
    """ Owns all worker agents """
    error = QtCore.Signal()

    def __init__(self, **kwargs):
        super().__init__(kwargs.pop('parent', None))
        self.worker_agents = {}
        if worker_agents := kwargs.get('agents'):
            for name, agent in worker_agents.items():
                self.worker_agents[name] = agent

    def add_agent(self, name):
        """ Adds a new sender """
        self.worker_agents[name] = agents.WorkerAgent(name, parent=self)

    def agent(self, name):
        """ Returns the worker agent """
        return self.worker_agents[name]

    def factory(self, name):
        """ Returns the descriptor factory """
        return descriptors.DescriptorFactory(self.worker_agents[name])

    def agent_factory(self, name):
        """ Returns the worker agent and the descriptor factory """
        return self.agent(name), self.factory(name)


worker_agency = WorkerAgency()


class FunctionWorker(QtCore.QObject):
    """ Worker thread that runs a user-supplied function """
    finished = QtCore.Signal()

    def __init__(self, function, *args, **kwargs):
        super().__init__(kwargs.pop('parent', None))
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.message = None

    def run(self):
        """ Run the function with exception handling """
        try:
            self.function(*self.args, **self.kwargs)
            self.finished.emit()
        except BaseException:
            (exception_type, value, traceback) = sys.exc_info()
            sys.excepthook(exception_type, value, traceback)


class GUIAgency(QtCore.QObject):
    """ Controller class which coordinates all figure and axis objects """
    gui_agents = {}

    @classmethod
    def add_container(cls, **containers):
        """ Add receivers """
        for name, container in containers.items():
            cls.gui_agents[name] = agents.GUIAgent(container)
        return cls

    def __init__(self, worker, *args, **kwargs):
        super().__init__(kwargs.pop('parent', None))
        self.exception_raised = False
        self.application = QtWidgets.QApplication(sys.argv)
        self.thread = QtCore.QThread()
        self.worker = FunctionWorker(worker, *args, **kwargs)
        self.worker_agency = worker_agency
        self.setup_worker()
        self.execute()

    def setup_worker(self):
        """ Setup worker thread """
        self.worker.moveToThread(self.thread)
        self.worker_agency.moveToThread(self.thread)
        for name, agent in self.gui_agents.items():
            self.worker_agency.agent(name).connect_agent(agent)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)


    def execute(self):
        """ Create QApplication, start worker thread and the main event loop """
        self.thread.start()
        try:
            self.application.exec_()
        except agents.WorkerAgentException:
            if not self.exception_raised:
                raise
            self.exception_raised = False
        finally:
            self.thread.terminate()
            self.thread.wait()
            self.application.exit()
            


    @QtCore.Slot()
    def worker_exception(self):
        """ Slot to react on a work exception """
        self.exception_raised = True
