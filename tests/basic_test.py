""" Test the pqthreads container module """

import pytest
from pqthreads.examples import window
from pqthreads.examples import gui_worker as gw


def test_basic():
    """ Basic functionality check, should not raise any errors """

    @gw.decorator
    def worker():
        """ Helper function """
        fig = gw.figure()
        fig.close()

    worker()


def test_method():
    """ Test return value of method call from the worker thread """

    @gw.decorator
    def worker():
        """ Helper function """
        fig = gw.figure()
        title = fig.change_title('Hello from worker')
        fig.close()
        return title

    result = worker()
    assert result == 'Figure 1: Hello from worker'

def test_attribute():
    """ Test attribute property """

    @gw.decorator
    def worker():
        """ Helper function """
        fig = gw.figure()
        fig.title = 'Hello from worker'
        title = fig.title
        fig.close()
        return title

    result = worker()
    assert result == 'Figure 1: Hello from worker'


def test_gui_exception():
    """ Test exception in GUI thread """

    @gw.decorator
    def worker():
        """ Helper function """
        fig = gw.figure()
        fig.raise_exception()
        fig.close()

    with pytest.raises(window.FigureWindowException):
        worker()


def test_worker_exception():
    """ Test exception in worker thread """

    @gw.decorator
    def worker():
        """ Helper function """
        fig = gw.figure()
        fig.raise_worker_exception()
        fig.close()

    with pytest.raises(gw.FigureWorkerException):
        worker()


def test_multiple_figure_closure():
    """ Test closure of multiple figures """

    @gw.decorator
    def worker():
        """ Helper function """
        fig1 = gw.figure()
        fig2 = gw.figure()
        fig3 = gw.figure()
        fig4 = gw.figure()
        fig1.close()
        fig3.close()
        fig2.close()
        fig4.close()

    try:
        worker()
    except IndexError:
        pytest.fail("Unexpected IndexError")
