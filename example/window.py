""" Figure window module """

import sys
try:
    from PySide6 import QtCore, QtWidgets
except ImportError:
    from PySide2 import QtCore, QtWidgets


class FigureWindow(QtWidgets.QMainWindow):
    """ Figure """

    def __init__(self, index, **kwargs):
        super().__init__(parent=kwargs.pop('parent', None))
        self.index = index
        self.resize(kwargs.get('width', 600), kwargs.get('height', 500))
        self.change_title(title=kwargs.get('title', 'Untitled'))
        self.show()

    def change_title(self, title='Untitled'):
        """ Change the window title """
        title = f'Figure {self.index+1}: {title}'
        self.setWindowTitle(title)
        return title

    def raise_window(self):
        """ Raises the current window to top """
        if sys.platform == 'win32':
            state = self.windowState() & ~QtCore.Qt.WindowMinimized | QtCore.Qt.WindowActive
            self.setWindowState(state)
            self.activateWindow()
        else:
            self.raise_()

    def delete(self):
        """ Closes the window """
        self.close()
