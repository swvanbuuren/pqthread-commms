""" Module with end user functions """

from pqthread_comms.examples import window
from pqthread_comms import controllers
from pqthread_comms import containers


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


class FigureTools: # pylint: disable=too-few-public-methods
    """ Provides end user functions """
    def __init__(self, worker_agency):
        agent = worker_agency.agent('figure')
        self.container = containers.WorkerItemContainer(item_class=FigureWorker.with_agent(agent))

    def figure(self, *args, **kwargs):
        """ Create, raise or modify FigureWorker objects """
        if not args:
            return self.container.create(**kwargs)
        figure_worker = args[0]
        self.container.current = figure_worker
        return figure_worker
