""" Module with helper class for decorator definition """

import functools
import wrapt
from pqthreads import controllers


class BaseDecoratorCore:
    """ Helper class for decorator definition """

    def __init__(self, **dec_kwargs):
        """ Reimplement this to make use of decorator's keyword arguments """
        self.gui_agency_class = controllers.GUIAgency
        self.add_gui_agents(self.gui_agency_class)

    @wrapt.decorator
    def __call__(self, wrapped, instance, args, kwargs):
        return self.wrapper(wrapped, args, kwargs)

    def wrapper(self, wrapped, args, kwargs):
        """ Simplified short hand for caller function """
        gui_agency = self.gui_agency_class(worker=wrapped, *args, **kwargs)
        self.add_worker_agents(gui_agency.worker_agency)
        gui_agency.execute()
        controllers.gui_refs.clear()
        controllers.worker_refs.clear()
        return gui_agency.result

    def add_gui_agents(self, gui_agency_class):
        """ Add GUI agents """
        raise NotImplementedError('This method must be implemented')

    def add_worker_agents(self, work_agency):
        """ Add worker agents """
        raise NotImplementedError('This method must be implemented')


class Decorator:
    """ Helper class for decorator definition """

    def __init__(self, decorator_class: BaseDecoratorCore):
        self.decorator_class = decorator_class

    def __call__(self, wrapped, **kwargs):
        """ Enables usage with and without decorator keyword arguments """
        if wrapped is None:
            return functools.partial(self.__call__, **kwargs)
        return self.decorator_class(**kwargs)(wrapped)
