# Pqthreads

Pqthreads exposes class interfaces from the main GUI Thread in another
QThread in Qt for Python. In doing so, it facilitates communication between the
main (GUI) thread and a dedicated `QThread`s as offered by [Qt for Python (PySide)](https://wiki.qt.io/Qt_for_Python).

## Design

Pqthreads separates the GUI elements from all programming elements in
`QThread`s. Since Qt demands that the main thread is used for GUI elements, all
other programming functionalities are moved into a dedicated `QThread`. This
shall be called the worker threads.

The following schematic depicts this design.

![Pqthreads design](doc/design.svg)

Communication between the GUI and worker threads is solely done using
Signal/Slot connections. This is faciliated by the GUI- and WorkerAgents.

The interface of a GUI Object is exposed by means of a Worker Object in the
Worker Thread.

It is possible expose the interface of mutiple types of GUI Objects (in the
shwon schematic `FigureWindow` and `GraphWindow`), which requires multiple
`Worker`- and `GUIAgent`s. These are helds the `GUIAgency` and `WorkerAgency`
respectively.

For each type of GUI/Worker object pair, it's also possible to instantiate
multiple objects (of the same type). GUI and Worker objects are held in the
`GUIItemContainer` and `WorkerItemContainer` respectively.

## License

An MIT style license applies for `pqthreads`, see the [LICENSE](LICENSE)
file for more details.
