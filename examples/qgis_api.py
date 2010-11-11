#!/usr/bin/env python
# -*- coding: utf-8 -*-
from qgis import core
core.QgsApplication.setPrefixPath("/usr", True)
core.QgsApplication.initQgis()

import os

wd = os.path.dirname(__file__)

vlayer = core.QgsVectorLayer(wd + "/../data/regioni.shp", "regioni", "ogr")
vlayer.isValid()

core.QgsMapLayerRegistry.instance().addMapLayer(vlayer)


from PyQt4 import QtGui, QtCore
img = QtGui.QImage(QtCore.QSize(800,600), QtGui.QImage.Format_ARGB32_Premultiplied)
p = QtGui.QPainter()
p.begin(img)

p.setRenderHint(QtGui.QPainter.Antialiasing)
render = core.QgsMapRenderer()
lst = [ vlayer.getLayerID() ]
render.setLayerSet(lst)
rect = core.QgsRectangle(render.fullExtent())
rect.scale(1.1)
render.setExtent(rect)
render.setOutputSize(img.size(), img.logicalDpiX())
img.size()
p.isActive()

render.render(p)
p.end()

img.save(wd + "/../images/regioni_qgis.png","png")
