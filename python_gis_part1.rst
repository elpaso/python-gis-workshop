.. title:: Developing Geospatial software with Python
.. footer:: GFOSS Day, Foligno - 18/19 November 2010

==================================================
Developing Geospatial software with Python, Part 1
==================================================

-----------------------------------------------------------------------
Alessandro Pasotti (apasotti@gmail.com), Paolo Corti (pcorti@gmail.com)
-----------------------------------------------------------------------

Building blocks
===============

Part 1 - Paolo Corti
* GDAL/OGR (Python bindings, GeoDjango, GeoAlchemy)
* GEOS (GeoDjango, Shapely)
* PROJ.4 (Python bindings, GeoDjango, GeoAlchemy)

Part 2 - Alessandro Pasotti
* OWS (OWSLib, pyWPS)
* WebServices (GeoPy, Mapnik, Mapscript)
* Desktop (QGIS, GRASS)

Building blocks: GDAL/OGR
=========================

* basic library for almost all FOSS4G projects (and often $$$ projects)
* library and utilities for reading/writing GIS formats
* raster/cover (GDAL) and vectorial (OGR)
* OGR follows the OGC Simple feature acces specifications
* written mostly in C++ by Frank Warmerdam
* license: MIT

GDAL/OGR: large diffusion
=========================

Huge list of sofware using GDAL, here only most important (full list @ GDAL website)

* FOSS4G: GRASS, GeoServer, gvSIG, MapServer, MapGuide, Orfeo Toolbox, OSSIM, QGIS, R
* $$$: ArcGis, ERDAS, FME, Google Earth

GDAL/OGR: many supported formats (vector)
=========================================

Long list too, here only most important (full list @gdalwebsite)

OGR (Vector):

* FOSS4G (RW): PostGis, Spatialite, MySQL, csv, GeoJSON, GeoRSS, GML, GPSBabel, GPX, GRASS, KML, WFS
* $$$: Shapefile, ArcInfo Coverage (R), ArcInfo .E00 (R), AutoCAD DXF, Esri PGDB (R), ArcSde (R), FMEObjects Gateway (R), MapInfo, Microstation DGN, Oracle Spatial, Microsoft MS Spatial

GDAL/OGR: many supported formats (raster)
=========================================

GDAL (Raster):

* FOSS4G (RW): GRASS Rasters, WKTRaster, Rasterlite
* $$$: ArcInfo ASCII Grid, ArcSde Raster (R), ERDAS (R), Oracle Spatial GeoRaster, Intergraph

GDAL/OGR: bindings
==================

bindings provide the GDAL power to developers using other languages than C/C++

* Python
* Perl
* VB6 (COM) - No SWIG
* Ruby
* Java
* .Net (VB, C#, ...)
* R

GDAL/OGR: command line utilities
================================

The power of GDAL/OGR at your fingertips (some written in python)!

* gdalinfo: info about a file
* gdal_translate: copy a raster with control on output
* gdal_rasterize: rasterize vectors
* gdalwarp: warp an image into a new coordiante system
* gdaltransform: transform coordinates
* gdal_retile.py: build tiled pyramid levels
* gdal_grid: create raster from scattered data
* gdal_polygonize.py: generate polygons from raster

Building blocks: GEOS
=====================

* it is a C++ port of JTS (Java Topology Suite di Vivid Solutions)
* originally started from Refractions for PostGIS
* provides all the OGC Simple Features for SQL spatial predicate functions and spatial operators
* license: LGPL

GEOS: API for modelling and manipulating 2-dimensional linear geometry
======================================================================

* model for geometric objects (Point, Linestring, Polygon, Multipoint, Multipolygon, GeomCollection)
* predicates and relationships (has_z, is_empty, is_valid, contains, crosses, equals, intersects, touches...)
* spatial analysis methods (boundary, centroid, difference, intersection, union, buffer, envelope, simplify...)
* interoperability (WKT, WKB)

GEOS: huge diffusion
====================

Huge list of sofware using GEOS, here only most important (full list @ GEOS website)

* FOSS4G: PostGIS, Spatialite, MapServer, QGIS, OGR, Shapely, GeoDjango
* $$$: FME, Autodesk MapGuide Enterprise

GEOS: bindings
==================

bindings provide the GEOS power to developers using other languages than C/C++

* Python (not manteined anymore --> GeoDjango, Shapely)
* Ruby
* PHP

Java developers of course must use the JTS!

.NET developers can use the .NET JTS port (NetTopologySuite)

Building blocks: PROJ.4
=======================

* PROJ.4 Cartographic Projections library originally written by Gerald Evenden then of the USGS
* written in c/c++
* both a command line and an API
* used from almost any FOSS4G project
* ported to js (Proj4js) and Java (Proj4J)
* license: MIT

PROJ.4: API
===========

Mainly 2 methods available:

1. create a projPJ coordinate system object from the string definition::

    projPJ pj_init_plus(const char *definition);

2. transform the x/y/z points from the source coordinate system to the destination coordinate system::

    int pj_transform( projPJ srcdefn, projPJ dstdefn, long point_count, int point_offset, double *x, double *y, double *z );

Notes on implementation
=======================

* pure Python (GeoAlchemy, GeoPy, OWSLib, pyWPS)

* Python and C/C++ libraries
    * with SWIG (GDAL/OGR bindings, Mapscript, GRASS, QGIS)
    * with ctypes (GeoDjango, Shapely, Mapnik)

GDAL/OGR bindings
=================

section about GDAL/OGR bindings

GeoDjango
=========

GeoAlchemy
==========

Shapely
=======


