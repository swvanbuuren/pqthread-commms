""" Testing of the pqthread_comms package """

import time
import gui
import worker

def main():
    """ Test function """

    time_delay = 0.25 # seconds

    fig1 = worker.figure(title='Initial title')
    fig1.change_title(title='Another title')

    time.sleep(time_delay)

    fig2 = worker.figure(title='Initial title')
    fig2.change_title('Latest title')

    time.sleep(time_delay)

    fig1.raise_window()

    time.sleep(time_delay)

    fig3 = worker.figure()

    time.sleep(time_delay)

    fig3.close()

    time.sleep(time_delay)

    fig2.close()
    fig1.close()


if __name__ == '__main__':
    gui.GUIAgency(worker=main)
