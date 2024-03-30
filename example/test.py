""" Testing of the pqthread_comms package """

import time
import gui_worker

def main():
    """ Test function """

    time_delay = 0.25 # seconds

    fig1 = gui_worker.figure(title='Initial title')
    fig1.change_title(title='Another title')

    time.sleep(time_delay)

    fig2 = gui_worker.figure(title='Initial title')
    fig2.change_title('Latest title')

    time.sleep(time_delay)

    fig1.raise_window()

    time.sleep(time_delay)

    fig3 = gui_worker.figure()

    time.sleep(time_delay)

    fig3.close()

    time.sleep(time_delay)

    fig2.close()
    fig1.close()


if __name__ == '__main__':
    gui_worker.GUIAgency(worker=main)
