""" Testing of the pqthread_comms package """

import time
from example import gui_worker

def main(agency):
    """ Test function """

    ft = gui_worker.FigureTools(agency)

    time_delay = 0.25 # seconds

    fig1 = ft.figure(title='Initial title')
    fig1.change_title(title='Another title')

    time.sleep(time_delay)

    fig2 = ft.figure(title='Initial title')
    fig2.change_title('Latest title')

    time.sleep(time_delay)

    fig1.raise_window()

    time.sleep(time_delay)

    fig3 = ft.figure()

    time.sleep(time_delay)

    fig3.close()

    time.sleep(time_delay)

    fig1.close()
    fig2.close()


if __name__ == '__main__':
    try:
        gui_worker.GUIAgency(worker=main)
    except IndexError:
        print('Unexpected Index error!')
    except RuntimeError:
        print('Unexpected Runtime error!')
