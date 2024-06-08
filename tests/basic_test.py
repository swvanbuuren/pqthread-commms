""" Test the pqthread_comms container module """

import pytest
from pqthread_comms.examples import window
from pqthread_comms.examples import gui_worker


def test_basic():
    """ Basic functionality check, should not raise any errors """

    def worker(agency: gui_worker.GUIAgency):
        """ Helper function """
        ft = gui_worker.FigureTools(agency)
        fig = ft.figure()
        fig.close()

    gui_worker.GUIAgency(worker=worker)


def test_method():
    """ Test return value of method call from the worker thread """

    def worker(agency: gui_worker.GUIAgency):
        """ Helper function """
        ft = gui_worker.FigureTools(agency)
        fig = ft.figure()
        title = fig.change_title('Hello from worker')
        fig.close()
        return title

    agency = gui_worker.GUIAgency(worker=worker)
    assert agency.result == 'Figure 1: Hello from worker'

def test_attribute():
    """ Test attribute property """

    def worker(agency: gui_worker.GUIAgency):
        """ Helper function """
        ft = gui_worker.FigureTools(agency)
        fig = ft.figure()
        fig.title = 'Hello from worker'
        title = fig.title
        fig.close()
        return title

    agency = gui_worker.GUIAgency(worker=worker)
    assert agency.result == 'Figure 1: Hello from worker'


def test_gui_exception():
    """ Test exception in GUI thread """

    def worker(agency: gui_worker.GUIAgency):
        """ Helper function """
        ft = gui_worker.FigureTools(agency)
        fig = ft.figure()
        fig.raise_exception()
        fig.close()

    with pytest.raises(window.FigureWindowException):
        gui_worker.GUIAgency(worker=worker)


def test_worker_exception():
    """ Test exception in worker thread """

    def worker(agency: gui_worker.GUIAgency):
        """ Helper function """
        ft = gui_worker.FigureTools(agency)
        fig = ft.figure()
        fig.raise_worker_exception()
        fig.close()

    with pytest.raises(gui_worker.FigureWorkerException):
        gui_worker.GUIAgency(worker=worker)


def test_multiple_figure_closure():
    """ Test closure of multiple figures """

    def worker(agency: gui_worker.GUIAgency):
        """ Helper function """
        ft = gui_worker.FigureTools(agency)
        fig1 = ft.figure()
        fig2 = ft.figure()
        fig3 = ft.figure()
        fig4 = ft.figure()
        fig1.close()
        fig3.close()
        fig2.close()
        fig4.close()

    try:
        gui_worker.GUIAgency(worker=worker)
    except IndexError:
        pytest.fail("Unexpected IndexError")
