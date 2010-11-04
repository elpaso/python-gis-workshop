#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys, subprocess
from ctypes import *
grass = CDLL("libgrass_gis.so")

if not os.environ.has_key("GISBASE"):
    print "You must be in GRASS GIS to run this program."
    sys.exit(1)

if len(sys.argv)==2:
  input = sys.argv[1]
else:
  input = raw_input("Raster Map Name? ")

# initialize
s = subprocess.Popen(['g.version','-r'], stdout=subprocess.PIPE).communicate()[0]
for line in s.splitlines():
    if line.startswith('Revision:'):
        version = '$' + line + '$'
grass.G__gisinit(version, '')

# find map in search path
mapset = grass.G_find_cell2(input, '')
mapset = c_char_p(mapset).value

# determine the inputmap type (CELL/FCELL/DCELL) */
data_type = grass.G_raster_map_type(input, mapset)

if data_type == 0:
    ptype = POINTER(c_int)
elif data_type == 1:
    ptype = POINTER(c_float)
elif data_type == 2:
    ptype = POINTER(c_double)

infd = grass.G_open_cell_old(input, mapset)
inrast = grass.G_allocate_raster_buf(data_type)
inrast = cast(c_void_p(inrast), ptype)

rows = grass.G_window_rows()
cols = grass.G_window_cols()

for rown in xrange(rows):
    grass.G_get_raster_row(infd, inrast, rown, data_type)
    print rown, inrast[0:cols]

grass.G_close_cell(infd)
grass.G_free(inrast)

