""" Test Controller implementation """

import figures
from pqthread_comms import controllers
from pqthread_comms import containers


figures_gui_container = containers.GUIItemContainer(figures.FigureWindow)

GUIAgency = controllers.GUIAgency
GUIAgency.add_container(figure=figures_gui_container)
