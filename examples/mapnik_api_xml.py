#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Adapted from: http://trac.mapnik.org/wiki/GettingStarted
import mapnik

import os
wd = os.path.dirname(os.path.realpath(__file__))

mapfile = 'mapnik_styles.xml'
m = mapnik.Map(600, 300)
mapnik.load_map(m, mapfile)
m.zoom_to_box(m.layers[0].envelope())
mapnik.render_to_file(m, wd + '/../images/regioni_mapnik_xml.png', 'png256')
