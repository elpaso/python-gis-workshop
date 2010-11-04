#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os

GISBASE = '/usr/lib/grass64/'
wd = os.path.dirname(os.path.realpath(__file__))

sys.path.append( GISBASE + 'etc/python/' )
os.environ['GISBASE'] = GISBASE
os.environ['GISRC'] = '/home/' + os.environ['USER'] + '/.grassrc6'
os.environ['PATH'] = os.environ['PATH'] + ':' + GISBASE + 'scripts/'
os.environ['PATH'] = os.environ['PATH'] + ':' + GISBASE + 'bin/'
os.environ['LD_LIBRARY_PATH'] = GISBASE + 'lib/'

import grass.script as grass

print grass.gisenv()
print grass.run_command('g.version', flags = 'r')

print wd + '/../data/regioni.shp'
print grass.run_command('v.in.ogr', flags = 'l', dsn = wd + '/../data/regioni.shp')

# Ctypes


import subprocess
from ctypes import *
grass = CDLL("libgrass_gis.so")

input = raw_input("Raster Map Name? ")

# initialize
s = subprocess.Popen(['g.version','-r'], stdout=subprocess.PIPE).communicate()[0]
for line in s.splitlines():
    if line.startswith('Revision:'):
        version = '$' + line + '$'
grass.G__gisinit(version, '')


