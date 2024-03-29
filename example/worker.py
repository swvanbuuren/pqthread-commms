""" Module with end user functions """

from pqthread_comms import controllers
from pqthread_comms import containers


# add agent on worker side
controllers.worker_agency.add_agent('figure')


class FigureWorker(containers.WorkerItem):
    """ Worker thread figure to control FigureWindow on the GUI thread"""
    controller, factory = controllers.worker_agency.agent_factory('figure')
    raise_window = factory.method()
    change_title = factory.method()


figures_worker_container = containers.WorkerItemContainer(item_class=FigureWorker)


def figure(*args, **kwargs):
    """ Create, raise or modify FigureWorker objects """
    if not args:
        return figures_worker_container.create(**kwargs)
    figure_worker = args[0]
    figures_worker_container.current = figure_worker
    return figure_worker
