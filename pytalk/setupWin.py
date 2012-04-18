from distutils.core import setup
import py2exe

setup(windows=[{"script":"pytalk.py"}], 
        options={"py2exe" : {"includes" : ["sip", "PyQt4._qt", "enum"]}})


