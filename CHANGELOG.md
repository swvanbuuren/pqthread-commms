# CHANGELOG

## v0.3.0 (2024-08-16)

### Feature

* feat(release): Add automatic semantic release

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`d5a1884`](https://github.com/swvanbuuren/pqthreads/commit/d5a1884e2e97547851855350ec97828a23428105))

### Unknown

* Bumpt to v0.3 for PyPi publishing

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`98d6d1c`](https://github.com/swvanbuuren/pqthreads/commit/98d6d1c8ba62e0dbd48b1f373b7d026801b25dd1))

* Correct version

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`8a5ac6f`](https://github.com/swvanbuuren/pqthreads/commit/8a5ac6f805afce44825b7e3c77abc35db053bf29))

## v0.2.0 (2024-08-15)

### Unknown

* Add link to PyPi package

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`e7f948a`](https://github.com/swvanbuuren/pqthreads/commit/e7f948a639c8ee3eb0fea6d31255e593ec515863))

* Move weak references into own module

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`74c02b4`](https://github.com/swvanbuuren/pqthreads/commit/74c02b401be15fb4bcbfc82dc6b57c3eca3ce699))

* Add installation instructions

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`6bdde70`](https://github.com/swvanbuuren/pqthreads/commit/6bdde70cae60039a40f047c8d22987d139238694))

* Fixes in usage instructions

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`07e63c5`](https://github.com/swvanbuuren/pqthreads/commit/07e63c5a9d83f780e786ffd5e13024495c314e63))

## v0.1.0 (2024-08-13)

### Unknown

* Add pittfalls section

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`3cd6e38`](https://github.com/swvanbuuren/pqthreads/commit/3cd6e38d4ac57f954e90a46fe58694aaf9c214e7))

* Add usage sections

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`c82e97b`](https://github.com/swvanbuuren/pqthreads/commit/c82e97ba93eda6209bc3782d4090774503398778))

* Add PyPi publishing workflow

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`6ab7d0d`](https://github.com/swvanbuuren/pqthreads/commit/6ab7d0d33623b2b9fb0bc7fb1d4d7f734d18dc03))

* Simplify decorator implementation

No need to subclass  DecoratorCore anymore. This is now only required when special functionality such as decorator arguments.

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`5512e23`](https://github.com/swvanbuuren/pqthreads/commit/5512e2343f846524e3ac978501eeb44bf764bfee))

* Take care of pylint warnings

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`bbd49de`](https://github.com/swvanbuuren/pqthreads/commit/bbd49de38c66fc661e98169fbce01f3d1e2ca23d))

* Move to advanced decorator setup

Use a class to define the decorator, making it easier to modify by subclassing.

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`d492cbf`](https://github.com/swvanbuuren/pqthreads/commit/d492cbfbc04d9e813c5fe325bffe73c090306d7d))

* Formatting in README

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`44e5e07`](https://github.com/swvanbuuren/pqthreads/commit/44e5e0773fcc58431dcf3547792cc346a3190074))

* Fix typos

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`3aad3df`](https://github.com/swvanbuuren/pqthreads/commit/3aad3df7b06e25b1ea88e6c49cc55879648c47c9))

* Add documentation on the design

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`50cd4b0`](https://github.com/swvanbuuren/pqthreads/commit/50cd4b043e74e4bbe544ba8b923f3fd4f4716519))

* Update actions name

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`b795ec0`](https://github.com/swvanbuuren/pqthreads/commit/b795ec048e444b8430798c09d0334e18272ebef1))

* Catch WorkerException also for PySide2

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`b55b594`](https://github.com/swvanbuuren/pqthreads/commit/b55b5948b12ef633573e94d3a25d8ee0b31e8e05))

* Modernize packaging setup with pyproject.toml

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`a59c4c9`](https://github.com/swvanbuuren/pqthreads/commit/a59c4c913404f8740b724d4b5dd0000500a15755))

* Issue premature signal_wait_stop using a simple method, not signal/slot connection

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`a4e4a67`](https://github.com/swvanbuuren/pqthreads/commit/a4e4a6714f00e9b56f83bb2635399bc3dde7af65))

* Make sure all GUI items in GUIItemContainer are destroyed during deletion

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`a975304`](https://github.com/swvanbuuren/pqthreads/commit/a9753040d18e255954b00b355b2cfd5f5e9ad038))

* Also have modify and request signal/slots wait for signals

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`7528081`](https://github.com/swvanbuuren/pqthreads/commit/7528081dc7004a4ef74cc35e5d8d7c48845cdd30))

* Fix closing order in multiple_figure_closure test

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`beebe1d`](https://github.com/swvanbuuren/pqthreads/commit/beebe1d118d963656a817123ec1254cb1cb25d6d))

* Clear Weak refs to worker and gui containers when done

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`de60747`](https://github.com/swvanbuuren/pqthreads/commit/de60747e27c85fde67ca21a713a3c456fe45fc70))

* Ignore pylint warning for GUIAgency

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`5154b59`](https://github.com/swvanbuuren/pqthreads/commit/5154b596e9540c52947f105f3ac820a02155f943))

* Get rid or unnecessary kickoff method in GUIAgency

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`f0cd7d9`](https://github.com/swvanbuuren/pqthreads/commit/f0cd7d94dabde041b53a3badabfefe2b7f43469a))

* Remove unused variable

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`969d387`](https://github.com/swvanbuuren/pqthreads/commit/969d3871398d172b3042df056ba29a475033970e))

* Setup GUI agents and containers with GUIAgency as parent

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`6f5df0e`](https://github.com/swvanbuuren/pqthreads/commit/6f5df0e3e3671bad3370d90b440cb2eec2c09d94))

* Store GUIItemContainer in GUIAgency class

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`4a6476c`](https://github.com/swvanbuuren/pqthreads/commit/4a6476c7f8ed7852a12fb0232f1119b74e952edd))

* Connect GUIAgent signals from method in GUIAgent class

Until now, the GUIAgent signals were connected to WorkerAgent slots in a WorkerAgent method

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`c48ba9d`](https://github.com/swvanbuuren/pqthreads/commit/c48ba9d73de68ee245411d1b1c072f202e4eb956))

* Remove redundant item deletion in GUI and WorkerItemContainer

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`5539d18`](https://github.com/swvanbuuren/pqthreads/commit/5539d18550bdbe83c581ab722f9b9a606d8d737b))

* Save item retrieval in GUIItemContainer

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`301dc1f`](https://github.com/swvanbuuren/pqthreads/commit/301dc1f3f974cc34b2d231e5c403300d1f63a733))

* Correct docstring of graph function

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`dd2c0bb`](https://github.com/swvanbuuren/pqthreads/commit/dd2c0bb251150c2a2bf1addf8f9e622f1769c886))

* Refactor WorkerAgent

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`ccacaeb`](https://github.com/swvanbuuren/pqthreads/commit/ccacaeb65e0b18188dc90028ed704619694f1f0b))

* Merge pull request #10 from swvanbuuren/swvanbuuren/wait-signal-class

Use class implementation for contextmanager wait_signal ([`45a979e`](https://github.com/swvanbuuren/pqthreads/commit/45a979eccb2978e7095598a7a8000f459128ae47))

* Use class implementation for contextmanager wait_signal

Using a class enables reuse of the context manager. This also avoids entering the same input arguments multiple times.

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`49208f2`](https://github.com/swvanbuuren/pqthreads/commit/49208f2a6bcb029f8c09dd1c02365a16064f8f1b))

* Merge pull request #9 from swvanbuuren/swvanbuuren/application-exit-after-thread-quit

Only exit application after thread stopped running or existing ([`d5abdbe`](https://github.com/swvanbuuren/pqthreads/commit/d5abdbed84b40a01f05cc5b164cef230075f6617))

* Only exit application after thread stopped running or became non-existent

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`9760c1f`](https://github.com/swvanbuuren/pqthreads/commit/9760c1f616602cfd0606e664e95f30700e23c922))

* Merge pull request #6 from swvanbuuren/swvanbuuren/fix-empty-worker

Application exit after thread finish without opened windows ([`ca2247c`](https://github.com/swvanbuuren/pqthreads/commit/ca2247c38c280969143799dfda55eeb1a5959510))

* Make the application exit after the thread has finished and no windows were opened

Also ads a corresponding test

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`007d3fa`](https://github.com/swvanbuuren/pqthreads/commit/007d3fa5b9a572aa3c56a83bbfdde482f07427c7))

* Introduce dedicated class method to instantiate DescriptorFactory on subclassed WorkerItems

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`1e0fcab`](https://github.com/swvanbuuren/pqthreads/commit/1e0fcab6e8411481a36b49588413bcc08116603a))

* Add test for multiple agent types

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`99567bd`](https://github.com/swvanbuuren/pqthreads/commit/99567bd15ab4bc7b601db9310cd84db49c66d68a))

* Add extra element for GUI and Worker named graph´

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`09a6727`](https://github.com/swvanbuuren/pqthreads/commit/09a67278ff8742627e779a566a31beea99829d84))

* Refactor WorkerAgency

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`147ac87`](https://github.com/swvanbuuren/pqthreads/commit/147ac87c1aeea201f87b957a9d04eeeb06c552a9))

* Make sure each Class inherited from WorkerItem has unique descriptor factory

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`d4ea5d0`](https://github.com/swvanbuuren/pqthreads/commit/d4ea5d0dec297026cf8040bf27be1798b415e572))

* Add name attribute for GUIAgent

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`8b345b1`](https://github.com/swvanbuuren/pqthreads/commit/8b345b112e353bdea547552177636d17bab3cbc6))

* Refactor GUIAgency class methods

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`6ca311f`](https://github.com/swvanbuuren/pqthreads/commit/6ca311fd6ea7841f21a37eeca757fe33c620889c))

* Distinguish between worker and gui type weak references

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`806a06a`](https://github.com/swvanbuuren/pqthreads/commit/806a06a7bb3720e26fe4cc9d43150b3c349d24a9))

* Change example module names

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`fb5f756`](https://github.com/swvanbuuren/pqthreads/commit/fb5f75677ad20611bd8d6c94c188931bc69556e7))

* Change naming from pqthread-comms to pqthreads

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`2991a19`](https://github.com/swvanbuuren/pqthreads/commit/2991a195adc7b452fd18ae6eeed3f2d416df515c))

* Add exception for missing weak referene

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`29efb7a`](https://github.com/swvanbuuren/pqthreads/commit/29efb7a6bff324d1f8f414bd0958bc9d4034f9a7))

* Adjust test for new decorator

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`f61253c`](https://github.com/swvanbuuren/pqthreads/commit/f61253c0aa90a6a560068a83ab4f481308193476))

* Adjust example for new decorator use

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`556c73b`](https://github.com/swvanbuuren/pqthreads/commit/556c73bae6249b975ae38f31442381912d089526))

* Adjust GUIAgency use for decorator and simplified usage in worker functions

GUIAgency now is setup at instantiation and started with an extra method. This allows to setup the GUIAgency in e.g. a decorator. In addition, weak references to worker containers are now stored at a module level, for easy access in decorated worker functions without additional definitions.

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`a656cbf`](https://github.com/swvanbuuren/pqthreads/commit/a656cbf1358202e6b20257e6a62abd74a58434ac))

* Change naming of controller to container in GUIAgent

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`263f570`](https://github.com/swvanbuuren/pqthreads/commit/263f5708990206129fa908232dc48cbbce8dd04d))

* Remove exception catch from example

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`5caba16`](https://github.com/swvanbuuren/pqthreads/commit/5caba1643b6604bd06e53832cc047a8bc5e7959a))

* Improve wording in README

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`f585cf8`](https://github.com/swvanbuuren/pqthreads/commit/f585cf807f9a46961fff46f13dd08baf845f37e3))

* Remove debug print message

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`c345cf0`](https://github.com/swvanbuuren/pqthreads/commit/c345cf0b363877a3bcb4d49865cc48685863efb8))

* Add test for proper worker exception handling

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`8308c43`](https://github.com/swvanbuuren/pqthreads/commit/8308c43895b07754c011044a5cba45eab6a1dcbb))

* Properly handle exceptions raised at worker side

Make sure all windows are closed in the GUI Thread, when a exception is raised in the Worker Thread.
Also refactor signal names for more clarity.

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`18ef771`](https://github.com/swvanbuuren/pqthreads/commit/18ef77129cd49f0ffda8f0261d1b1e8a5ef8e9da))

* Make sure eventloops are quit on errors

Refactor signal names for quit eventloops in Worker Agents. Also quit eventloops in Worker Agent destructor.

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`74f1f8a`](https://github.com/swvanbuuren/pqthreads/commit/74f1f8a8877999f1275b869c6ecd74a10cdb57de))

* Remove debug print statement

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`37b57e2`](https://github.com/swvanbuuren/pqthreads/commit/37b57e2f64455ac3b9df33d7b75e70642a0caeae))

* Abort eventloops in the worker thread in case of exceptions in the GUI thread

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`d7d6ca6`](https://github.com/swvanbuuren/pqthreads/commit/d7d6ca699a592a020b6d8d610e9a606c3bfdb36e))

* User stop_thread method also after caught exception

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`be0fce9`](https://github.com/swvanbuuren/pqthreads/commit/be0fce964da1daf3df90df8d3aff5d3c39a4cd88))

* Enable verbose output of pytest

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`29c5000`](https://github.com/swvanbuuren/pqthreads/commit/29c500055e081594b65ebf261ce1e881a49826cc))

* Change worker thread quit mechanism

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`2bc474e`](https://github.com/swvanbuuren/pqthreads/commit/2bc474e8e0522baa38c93808872c7c41f9eca9ff))

* Another try with xvfb to run tests on GHA

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`eb23ba5`](https://github.com/swvanbuuren/pqthreads/commit/eb23ba5e9f702aa4940fe6f79fd6462c558c64c8))

* Add more missing dependencies for testing

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`5a37c64`](https://github.com/swvanbuuren/pqthreads/commit/5a37c640066cea2760fa416e9673fe0466c37e09))

* Add special test dependencies

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`9ac0776`](https://github.com/swvanbuuren/pqthreads/commit/9ac07761f6a1dca6e673546e1a1d2c37bba434fb))

* Add OS dependencies for PySide6

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`b30c707`](https://github.com/swvanbuuren/pqthreads/commit/b30c707e2b9ee028d6f0931e5c0f001ba2fb29f7))

* Add package requirements

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`7a08bcb`](https://github.com/swvanbuuren/pqthreads/commit/7a08bcbc0049deaf75e05dc10bbb79cd59cce902))

* Add init file to tests directory

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`87a5b26`](https://github.com/swvanbuuren/pqthreads/commit/87a5b262778bccef4874c1f049d62b2406519eb8))

* Fix linter error

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`a664194`](https://github.com/swvanbuuren/pqthreads/commit/a664194f0f1ff9ff4beef33369513b601045f2b2))

* Change example structure

But jointly used files for examples and test in dedicated examples directory in the source package

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`d334702`](https://github.com/swvanbuuren/pqthreads/commit/d3347029a5396eccb439314031d9532bf2ec0f77))

* Change naming of test directory

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`f05eae2`](https://github.com/swvanbuuren/pqthreads/commit/f05eae2282d921ea93dc98184aa187da37373a56))

* Change naming of examples directory

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`9a85a44`](https://github.com/swvanbuuren/pqthreads/commit/9a85a4485546b9646488fb4b1a5234f24c7ae876))

* Setup automatic linting with pylint and testing with pytest

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`8cac42d`](https://github.com/swvanbuuren/pqthreads/commit/8cac42d3ad146351957d441abb0b840dc0906671))

* Fix or Ignore linter errors for pylint

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`1bf134d`](https://github.com/swvanbuuren/pqthreads/commit/1bf134df6f4e13da03ad67002fe4e98c23648616))

* Ignore pytest cache

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`2187753`](https://github.com/swvanbuuren/pqthreads/commit/21877533625817f550830af889ea53e26e08932b))

* Add tests for attribute property and custom exception
Improve test for multiple figure closure

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`e20eb6b`](https://github.com/swvanbuuren/pqthreads/commit/e20eb6bcfa4e90ade1895856343a11e143dd0768))

* Add indices for each GUIItemContainer for persistent index values

Necessary to delete item using index that doesn´t change, e.g. when another item is deleted

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`7c4e92b`](https://github.com/swvanbuuren/pqthreads/commit/7c4e92b485f605b241315d4173d26b3b71f6824d))

* Simplify error/exception handling

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`573ce97`](https://github.com/swvanbuuren/pqthreads/commit/573ce97ac5f5466c7fcd459d7de6b778d671afdb))

* Move waitsignal contextmanager to utils module

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`7a9c7a7`](https://github.com/swvanbuuren/pqthreads/commit/7a9c7a7b02b4beacb9c6bfcc56d7f4fb903a94d9))

* First exit thread before exiting application on excepthool

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`722bcd9`](https://github.com/swvanbuuren/pqthreads/commit/722bcd9cf6408d79a38b7f62018bf7730adc6721))

* Make sure exceptions are propagated correctly in the GUI Thread, so they can be caught

Add a test to catches an exception

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`5b20bf3`](https://github.com/swvanbuuren/pqthreads/commit/5b20bf3a43e105535adabc4fba931dc0fd808fab))

* Improve short description

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`ad0883d`](https://github.com/swvanbuuren/pqthreads/commit/ad0883d2f66ff4170300b7cdc808765fe40c46ea))

* Update year in LICENSE

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`3e22bb7`](https://github.com/swvanbuuren/pqthreads/commit/3e22bb7e188e1f4bab397fdd5fd30151009dc2bc))

* General cleanup and removal of global singleton variables

Getting rid of persistent variables at module level enables to repeatedly perform tests. To show this, two basic pytest tests were added.

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`aa3b9be`](https://github.com/swvanbuuren/pqthreads/commit/aa3b9bebdd6c8921b99a83e04304f4006969b9c5))

* Add backwards compatibl exec() calls

Uses  exec_() calls for PySide2 and exec() calls for PySide6

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`2d6bd71`](https://github.com/swvanbuuren/pqthreads/commit/2d6bd71b910165c8efd4b35d05fe6774c157cc21))

* Simplify the example

Reduce the number of file, combine gui and worker thread setup in one file

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`7058783`](https://github.com/swvanbuuren/pqthreads/commit/70587835150e637a831abab49c24f365e7a6c40c))

* Change the way QThread is ended

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`6ff64a3`](https://github.com/swvanbuuren/pqthreads/commit/6ff64a3351166981ff1dc71017085920031f9d36))

* Example with Figure (QMainWindow)

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`6fdc9c6`](https://github.com/swvanbuuren/pqthreads/commit/6fdc9c66d6792a2a319f037202f4ca765f1c2fa9))

* Design documentation

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`b84f4c6`](https://github.com/swvanbuuren/pqthreads/commit/b84f4c68681888c4238b568e3ccdc84f6650f400))

* First functional package

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`dcb401c`](https://github.com/swvanbuuren/pqthreads/commit/dcb401c00989cb134ea8c9fe44e415c65fee1cb4))

* Fix typo in README

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`6dcffe1`](https://github.com/swvanbuuren/pqthreads/commit/6dcffe107eff077fa5caf254761edc8acad5767c))

* Initial commit

Signed-off-by: Sietze van Buuren &lt;s.van.buuren@gmail.com&gt; ([`6ccfbda`](https://github.com/swvanbuuren/pqthreads/commit/6ccfbdae939739cc87b36c507e25a76fd0664a8f))
