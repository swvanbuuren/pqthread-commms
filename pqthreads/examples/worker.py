""" Module with end user functions """

from pqthreads.examples import window
from pqthreads import controllers
from pqthreads import containers


class FigureWorkerException(Exception):
    """ Exception for FigureWorker """


# Setup GUI side
GUIAgency = controllers.GUIAgency
GUIAgency.add_gui_items(figure=window.FigureWindow)


# Setup worker side
class FigureWorker(containers.WorkerItem):
    """ Worker thread figure to control FigureWindow on the GUI thread"""
    factory = containers.WorkerItem.factory
    raise_window = factory.method()
    change_title = factory.method()
    title = factory.attribute()
    raise_exception = factory.method()

    def raise_worker_exception(self):
        """ Method to raise custom exception for testing purposes """
        raise FigureWorkerException('Custom exception')


def figure(*args, **kwargs):
    """ Create, raise or modify FigureWorker objects """
    container = controllers.worker_refs.get('figure')
    if not args:
        return container.create(**kwargs)
    figure_worker = args[0]
    container.current = figure_worker
    return figure_worker


def decorator(func):
    """ Decorator for end user functions, adding figure functionality"""
    def wrapper():
        """ Wrapper """
        gui_agency = GUIAgency(worker=func)
        gui_agency.worker_agency.add_container('figure', FigureWorker)
        gui_agency.kickoff()
        return gui_agency.result
    return wrapper
