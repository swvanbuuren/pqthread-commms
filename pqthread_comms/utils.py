""" Utility module """

try:
    import PySide6 as PySide
except ImportError:
    import PySide2 as PySide

def compat_exec(obj):
    """ Compatibility exec function """
    if PySide.__version_info__[0] < 6:
        obj.exec_()
    else:
        obj.exec()
