#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Adapted from: http://trac.mapnik.org/wiki/GettingStarted
import mapnik

import os
wd = os.path.dirname(os.path.realpath(__file__))


# Instantiate a map object with given width, height and spatial reference system
m = mapnik.Map(300,300,"+proj=latlong +datum=WGS84")
# Set background colour to 'steelblue'.
# You can use 'named' colours, #rrggbb, #rgb or rgb(r%,g%,b%) format
m.background = mapnik.Color('steelblue')
# Now lets create a style and add it to the Map.
s = mapnik.Style()
# A Style can have one or more rules. A rule consists of a filter, min/max scale
# demoninators and 1..N Symbolizers. If you don't specify filter and scale denominators
# you get default values :
#   Filter =  'ALL' filter (meaning symbolizer(s) will be applied to all features)
#   MinScaleDenominator = 0
#   MaxScaleDenominator = INF
# Lets keep things simple and use default value, but to create a map we
# we still must provide at least one Symbolizer. Here we  want to fill countries polygons with
# greyish colour and draw outlines with a bit darker stroke.

r = mapnik.Rule()
r.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color('#f2eff9')))
r.symbols.append(mapnik.LineSymbolizer(mapnik.Color('rgb(50%,50%,50%)'),0.1))
s.rules.append(r)

# Make PIEDMONT red
f = mapnik.Filter("[regione] = 'PIEMONTE'")
r = mapnik.Rule()
r.filter = f
r.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color('#ff0000')))
s.rules.append(r)

m.append_style('My Style',s)

# Here we instantiate our data layer, first by giving it a name and srs (proj4 projections string), and then by giving it a datasource.
lyr = mapnik.Layer('world',"+proj=latlong +datum=WGS84")
# Then provide the full filesystem path to a shapefile in WGS84 or EPSG 4326 projection without the .shp extension
# A sample shapefile can be downloaded from http://mapnik-utils.googlecode.com/svn/data/world_borders.zip
lyr.datasource = mapnik.Shapefile(file = wd + '/../data/regioni')
lyr.styles.append('My Style')
m.layers.append(lyr)
m.zoom_to_box(lyr.envelope())
mapnik.render_to_file(m, wd + '/../images/regioni_mapnik.png', 'png256')


# Feature explore
feature = lyr.datasource.all_features()[0]
for p in feature.attributes:
    p

