""" Backwards compatible PySide imports """

try:
    import PySide6 as PySide
    from PySide6 import QtCore, QtWidgets
except ImportError:
    import PySide2 as PySide
    from PySide2 import QtCore, QtWidgets
