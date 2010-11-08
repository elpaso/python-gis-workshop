#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os

GISBASE = '/usr/lib/grass64/'
wd = os.path.dirname(os.path.realpath(__file__))

# Setup environment
sys.path.append( GISBASE + 'etc/python/' )
os.environ['GISBASE'] = GISBASE
os.environ['GISRC'] = '/home/' + os.environ['USER'] + '/.grassrc6'
os.environ['PATH'] = os.environ['PATH'] + ':' + GISBASE + 'scripts/'
os.environ['PATH'] = os.environ['PATH'] + ':' + GISBASE + 'bin/'
os.environ['LD_LIBRARY_PATH'] = GISBASE + 'lib/'
os.environ['GIS_LOCK'] = "%s" % os.getpid()

import grass.script as grass

print grass.gisenv()

import shutil
try:
    shutil.rmtree(grass.gisenv()['GISDBASE'] + '/regioni')
except:
    pass     

print grass.run_command('g.version', flags = 'r')
print grass.run_command('v.in.ogr', flags = 'l', dsn = wd + '/../data/regioni.shp')
print grass.run_command('v.in.ogr', flags='c', layer = 'regioni', location = 'regioni', output = 'regioni',  dsn = wd + '/../data/regioni.shp')
# Set region resolution
print grass.run_command('g.mapset', mapset='PERMANENT', location='regioni')
print grass.run_command('g.region', res = 0.02)
print grass.run_command('g.list',  type = 'vect')
print grass.run_command('v.to.rast', input='regioni', output='regioni', column='cod_reg')
print grass.run_command('r.out.png', input='regioni', output= wd + '/../images/regioni_grass.png')

