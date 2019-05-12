The procedure to install dependencies in windows isn't so easy as in POSIX. I'll try to explain here the procedure.

Current versions:
    * python v3.7
    * Procedure checked in windows 7 and windows 10

Using Anaconda
--------------
If the disk space isn't problem, we can install a python distribution with full of packages to boost it, like anaconda:

    * x86: https://repo.anaconda.com/archive/Anaconda3-2019.03-Windows-x86.exe
    * amd64: https://repo.anaconda.com/archive/Anaconda3-2019.03-Windows-x86_64.exe


Install only python and neccessary library
------------------------------------------

First we need install python3, from his `page <https://www.python.org/downloads/release/python-373/>`__, it depends of your computer architecture, x86, x86-64:

    * x86: https://www.python.org/ftp/python/3.7.3/python-3.7.3-webinstall.exe
    * amd64: https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64-webinstall.exe

Now using the pip command shipped with python we can install dependencies easy. Open a cmd console and run:

    * py -m pip install pyside2

Get jmbde-Python code
-----------------

To get jmbde-Python download the zip file from https://github.com/jmuelbert/jmbde-python/archive/master.zip and unzip whatever you want. To run doble click over the main script jmbde.py.