""" Module with end user functions """

from pqthreads.examples import window
from pqthreads import controllers
from pqthreads import containers
from pqthreads import decorator


class FigureWorkerException(Exception):
    """ Exception for FigureWorker """


# Setup worker side
class FigureWorker(containers.WorkerItem):
    """ Worker thread figure to control FigureWindow on the GUI thread"""
    factory = containers.WorkerItem.get_factory()
    raise_window = factory.method()
    change_title = factory.method()
    title = factory.attribute()
    raise_exception = factory.method()

    def raise_worker_exception(self):
        """ Method to raise custom exception for testing purposes """
        raise FigureWorkerException('Custom exception')


class GraphWorker(containers.WorkerItem):
    """ Worker thread graph to control GraphWindow on the GUI thread"""
    factory = containers.WorkerItem.get_factory()
    test_method = factory.method()


def figure(*args, **kwargs):
    """ Create, raise or modify FigureWorker objects """
    container = controllers.worker_refs.get('figure')
    if not args:
        return container.create(**kwargs)
    figure_worker = args[0]
    container.current = figure_worker
    return figure_worker


def graph(*args, **kwargs):
    """ Create, raise or modify GraphWorker objects """
    container = controllers.worker_refs.get('graph')
    if not args:
        return container.create(**kwargs)
    graph_worker = args[0]
    container.current = graph_worker
    return graph_worker

# Configure decorators
class DecoratorCore(decorator.BaseDecoratorCore):
    """ Helper class for decorator definition """

    def add_gui_agents(self, gui_agency_class):
        """ Add GUI agents """
        gui_agency_class.add_agent('figure', window.FigureWindow)
        gui_agency_class.add_agent('graph', window.GraphWindow)

    def add_worker_agents(self, work_agency):
        """ Add worker agents """
        work_agency.add_container('figure', FigureWorker)
        work_agency.add_container('graph', GraphWorker)


decorator_example = decorator.Decorator(DecoratorCore)
