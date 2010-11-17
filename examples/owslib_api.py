#!/usr/bin/env python                                                                              
# -*- coding: utf-8 -*-                                                                            

from owslib.wms import WebMapService
wms = WebMapService('http://wms.pcn.minambiente.it/cgi-bin/mapserv.exe?map=/ms_ogc/service/ortofoto_colore_06_f32.map', version='1.1.1')
list(wms.contents)
wms.contents['ortofoto_colore_06']
wms['ortofoto_colore_06'].boundingBox
wms['ortofoto_colore_06'].boundingBoxWGS84

