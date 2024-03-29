""" GUI Item module """

import weakref
try:
    from PySide6 import QtCore
except ImportError:
    from PySide2 import QtCore


class RootException(Exception):
    """ Root Exception of the threads module """


class ItemException(RootException):
    """ This Exception is raised if an error was raised in the worker thread """


class GUIItemContainer(QtCore.QObject):
    """
    Controller for a container with instances of user-supplied GUI element class
    """

    def __init__(self, item_class, parent=None):
        super().__init__(parent)
        self.items = []
        self.item_class = item_class

    def __repr__(self):
        return f'{self.__class__.__name__}(item_class={self.item_class.__name__})'

    @property
    def count(self):
        """ Current number of items """
        return len(self.items)

    def back(self):
        """ Returns the last item """
        return self.items[-1]

    def create(self, args, kwargs):
        """ Creates a new item instance with user-supplied item class """
        index = self.count
        new_item = self.item_class(index, *args, **kwargs)
        self.items.append(new_item)
        return index

    def request(self, index, args):
        """ Returns values of item attributes """
        item = self.items[index]
        return [getattr(item, arg) for arg in args]

    def modify(self, index, kwargs):
        """ Modifies item's attributes"""
        item = self.items[index]
        for key, value in kwargs.items():
            setattr(item, key, value)

    def method(self, index, func_name, args, kwargs):
        """ Execute method on item """
        try:
            item = self.items[index]
        except IndexError as err:
            raise ItemException(f'Index not find for {self.item_class} items') from err
        func = getattr(item, func_name)
        return func(*args, **kwargs)

    def delete(self, index):
        """ Deletes the item at index """
        item = self.items.pop(index)
        item.delete()
        del item


class WorkerItem:
    """ Abstract Worker Item class """
    controller = None

    def __init__(self, *args, **kwargs):
        self.index = self.controller.create(*args, **kwargs)

    def __repr__(self):
        return f'{self.__class__.__name__}(index={self.index})'

    def close(self):
        """ Closes the current figure on the GUI side """
        self.controller.delete(self.index)


class WorkerItemContainer:
    """ Abstract Worker Item Container class """

    def __init__(self, item_class):
        self.item_class = item_class
        self.items = []
        self.current = None

    def __repr__(self):
        repr_string = '['
        for idx, figure in enumerate(self.items):
            if idx > 0:
                repr_string += ', '
            repr_string += repr(figure)
        repr_string += ']'
        return repr_string

    def create(self, *args, **kwargs):
        """ Create a new FigureWorker and return a weak reference proxy """
        self.append(self.item_class(*args, **kwargs))
        self.current = self.back()
        return weakref.proxy(self.back())

    def append(self, item):
        """ Append an item """
        self.items.append(item)

    def back(self):
        """ Returns the last item """
        return self.items[-1]

    def close(self, item):
        """
        Remove an item from the container, closes its figure and deletes it.
        After calling this function, weak references to this item will no longer
        be valid.
        """
        index = self.items.index(item)
        worker_item = self.items.pop(index)
        worker_item.close()
        del worker_item
