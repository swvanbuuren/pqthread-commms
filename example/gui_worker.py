""" Module with end user functions """

import window
from pqthread_comms import controllers
from pqthread_comms import containers


# Setup worker side
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


# Setup GUI side
figures_gui_container = containers.GUIItemContainer(window.FigureWindow)

GUIAgency = controllers.GUIAgency
GUIAgency.add_container(figure=figures_gui_container)
