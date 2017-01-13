#!/usr/bin/python
#-*-coding: UTF-8-*-
import subprocess
import sys, os, getopt
sys.path.append(os.path.join(os.path.dirname(__file__), '.', 'repositories'))
from mongodataaccessbase import *
from sqldataaccessbase import *