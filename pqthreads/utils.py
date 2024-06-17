""" Utility module """

from contextlib import contextmanager
from pqthreads.qt import PySide
from pqthreads.qt import QtCore


def compat_exec(obj):
    """ Compatibility exec function """
    if PySide.__version_info__[0] < 6:
        obj.exec_()
    else:
        obj.exec()


@contextmanager
def wait_signal(signal, error_signal=None, timeout=1000):
    """Block loop until signal emitted, or timeout (ms) elapses."""
    loop = QtCore.QEventLoop()
    signal.connect(loop.quit)
    if error_signal is not None:
        error_signal.connect(loop.quit)
    yield
    if timeout is not None:
        QtCore.QTimer.singleShot(timeout, loop.quit)
    compat_exec(loop)
