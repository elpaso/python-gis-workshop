#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Example: mapscript
#

import mapscript, os


def main:
    map = mapscript.mapObj()
    map.name = 'Test Map'
    map.setSize(300, 300)
    map.setExtent(-180.0,-90.0,180.0,90.0)
    map.imagecolor.setRGB(80, 180, 80)
    map.units = mapscript.MS_DD

    layer = mapscript.layerObj(map)
    layer.name = "regioni"
    layer.type = mapscript.MS_LAYER_POLYGON
    layer.status = mapscript.MS_DEFAULT
    layer.data = os.getcwd() + '/../data/regioni'

    class1 = mapscript.classObj(layer)
    class1.name = "Regioni"
    style = mapscript.styleObj(class1)
    style.outlinecolor.setRGB(100, 100, 100)
    style.color.setRGB(200, 200, 200)
    extent = layer.getExtent()

    map.setExtent(extent.minx, extent.miny, extent.maxx, extent.maxy)
    mapimage = map.draw()

    mapimage.save(os.getcwd() + '/../images/mapscript_map.png')

if __name__ == "__main__":
    main()
