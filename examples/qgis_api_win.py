#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
import sys, os
from qgis import core, gui

core.QgsApplication.setPrefixPath('/usr', True)
core.QgsApplication.initQgis()

l = core.QgsVectorLayer(sys.argv[1], os.path.basename(sys.argv[1]), 'ogr')
app = QtGui.QApplication(sys.argv)
canvas = gui.QgsMapCanvas()
canvas.resize(800,600)
core.QgsMapLayerRegistry.instance().addMapLayer(l)
canvas.setExtent(l.extent())
cl = gui.QgsMapCanvasLayer(l)
layers = [cl]
canvas.setLayerSet(layers)
canvas.show()
retval = app.exec_()
core.QgsApplication.exitQgis()
sys.exit(retval)
