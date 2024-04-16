""" Utility module """

from pqthread_comms.qt import PySide

def compat_exec(obj):
    """ Compatibility exec function """
    if PySide.__version_info__[0] < 6:
        obj.exec_()
    else:
        obj.exec()
