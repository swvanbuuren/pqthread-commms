""" Module with end user functions """

from example import window
from pqthread_comms import controllers
from pqthread_comms import containers


# Setup GUI side
GUIAgency = controllers.GUIAgency
GUIAgency.add_gui_items(figure=window.FigureWindow)

# Setup worker side
class FigureWorker(containers.WorkerItem):
    """ Worker thread figure to control FigureWindow on the GUI thread"""
    factory = containers.WorkerItem.factory
    raise_window = factory.method()
    change_title = factory.method()


class FigureTools:
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
