# -*- coding: utf-8 -*-
from qgis.gui import *
from qgis.core import *
QgsApplication.setPrefixPath("/usr", True)
QgsApplication.initQgis()

import os

wd = os.getcwd()

vlayer = QgsVectorLayer(wd + "/../data/regioni.shp", "regioni", "ogr")
vlayer.isValid()

QgsMapLayerRegistry.instance().addMapLayer(vlayer)
from PyQt4.QtGui import *
from PyQt4.QtCore import *
img = QImage(QSize(800,600), QImage.Format_ARGB32_Premultiplied)
p = QPainter()
p.begin(img)

p.setRenderHint(QPainter.Antialiasing)
render = QgsMapRenderer()
lst = [ vlayer.getLayerID() ]
render.setLayerSet(lst)
rect = QgsRectangle(render.fullExtent())
rect.scale(1.1)
render.setExtent(rect)
render.setOutputSize(img.size(), img.logicalDpiX())
img.size()
p.isActive()

render.render(p)
p.end()

img.save(wd + "/../images/render.png","png")
