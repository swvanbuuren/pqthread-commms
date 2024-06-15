""" Testing of the pqthread_comms package """

import time
from pqthread_comms.examples import gui_worker as gw


@gw.decorator
def main():
    """ Test function """

    time_delay = 0.25 # seconds

    fig1 = gw.figure(title='Initial title')
    fig1.change_title(title='Another title')

    time.sleep(time_delay)

    fig2 = gw.figure(title='Initial title')
    fig2.change_title('Latest title')

    time.sleep(time_delay)

    fig1.raise_window()

    time.sleep(time_delay)

    fig3 = gw.figure()

    time.sleep(time_delay)

    fig3.close()

    time.sleep(time_delay)

    fig1.close()
    fig2.close()


if __name__ == '__main__':
    main()
