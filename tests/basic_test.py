""" Test the pqthreads container module """

import pytest
from pqthreads.examples import window
from pqthreads.examples import worker


def test_basic():
    """ Basic functionality check, should not raise any errors """

    @worker.decorator
    def main():
        """ Helper function """
        fig = worker.figure()
        fig.close()

    main()


def test_method():
    """ Test return value of method call from the worker thread """

    @worker.decorator
    def main():
        """ Helper function """
        fig = worker.figure()
        title = fig.change_title('Hello from worker')
        fig.close()
        return title

    result = main()
    assert result == 'Figure 1: Hello from worker'

def test_attribute():
    """ Test attribute property """

    @worker.decorator
    def main():
        """ Helper function """
        fig = worker.figure()
        fig.title = 'Hello from worker'
        title = fig.title
        fig.close()
        return title

    result = main()
    assert result == 'Figure 1: Hello from worker'


def test_gui_exception():
    """ Test exception in GUI thread """

    @worker.decorator
    def main():
        """ Helper function """
        fig = worker.figure()
        fig.raise_exception()
        fig.close()

    with pytest.raises(window.FigureWindowException):
        main()


def test_worker_exception():
    """ Test exception in worker thread """

    @worker.decorator
    def main():
        """ Helper function """
        fig = worker.figure()
        fig.raise_worker_exception()
        fig.close()

    with pytest.raises(worker.FigureWorkerException):
        main()


def test_multiple_figure_closure():
    """ Test closure of multiple figures """

    @worker.decorator
    def main():
        """ Helper function """
        fig1 = worker.figure()
        fig2 = worker.figure()
        fig3 = worker.figure()
        fig4 = worker.figure()
        fig1.close()
        fig3.close()
        fig2.close()
        fig4.close()

    try:
        main()
    except IndexError:
        pytest.fail("Unexpected IndexError")


def test_multiple_agent_types():
    """ Test functionality of multiple agent types """

    @worker.decorator
    def main():
        """ Helper function """
        fig = worker.figure()
        graph = worker.graph()
        result = graph.test_method()
        fig.close()
        graph.close()
        return result

    result = main()
    assert result == 'Test successful'
