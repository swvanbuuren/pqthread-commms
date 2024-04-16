""" Test the pqthread_comms container module """

from example import gui_worker


def test_no_exceptions():
    """ Test that no exceptions are raised """
    
    def main(agency):
        """ Helper function to test the container """
        ft = gui_worker.FigureTools(agency)
        fig = ft.figure()
        fig.close()

    gui_worker.GUIAgency(worker=main)


def test_method():
    """ Test calling method on the GUI thread from the worker thread """

    def worker(agency):
        """ Worker function to test calling method on GUI thread """
        ft = gui_worker.FigureTools(agency)
        fig = ft.figure()
        title = fig.change_title('Hello from worker')
        fig.close()
        return title

    agency = gui_worker.GUIAgency(worker=worker)
    assert agency.result == 'Figure 1: Hello from worker'
