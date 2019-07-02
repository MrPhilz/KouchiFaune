# -*- coding: utf-8 -*-

import arcpy
import pythonaddins
import os

class ButtonClass1(object):
    """Implementation for addin_addin.button_1 (Button)"""

    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        print "Choix d'un repertoire de travail, ainsi que l'image a classifier..."
        global wdPath
        wdPath = pythonaddins.OpenDialog("Selectionnez un repertoire de travail...", False, "C:", "Ajouter")
        global rasterPath
        rasterPath = pythonaddins.OpenDialog("Selectionnez une couche matricielle...", False, "C:", "Ajouter")
        print rasterPath

        arcpy.MakeRasterLayer_management(rasterPath, "rasterLayer")

class ButtonClass2(object):
    """Implementation for addin_addin.button_2 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
        self.shape = "NONE"
    def onClick(self):
        arcpy.env.overwriteOutput = True
        print "Creation d'un masque..."
        arcpy.CreateFeatureclass_management(wdPath, "mask.shp", "POLYGON")
        # self.maskCoord = arcpy.Array()
        print "Clip de la couche matricielle: " + rasterPath
    def onMouseDownMap(self, x, y):
        message = "Your mouse clicked:" + str(x) + ", " + str(y)
        pythonaddins.MessageBox(message, "My Coordinates")

class ButtonClass3(object):
    """Implementation for addin_addin.button_3 (Button)"""
    def __init__(self):
        self.enabled = False
        self.checked = False
    def onClick(self):
        print "Debut de la creation des sites d'entrainement pour la classe: " + selectedClass

class ButtonClass4(object):
    """Implementation for addin_addin.button_4 (Button)"""
    def __init__(self):
        self.enabled = False
        self.checked = False
    def onClick(self):
        print "Classification de la couche matricielle..."

class ButtonClass5(object):
    """Implementation for addin_addin.button_5 (Button)"""
    def __init__(self):
        self.enabled = False
        self.checked = False
    def onClick(self):
        print "Nettoyage de la couche matricielle..."

class ButtonClass6(object):
    """Implementation for addin_addin.button_6 (Button)"""
    def __init__(self):
        self.enabled = False
        self.checked = False
    def onClick(self):
        print "Vectorisation de la couche matricielle..."

class ButtonClass7(object):
    """Implementation for addin_addin.button_7 (Button)"""
    def __init__(self):
        self.enabled = False
        self.checked = False
    def onClick(self):
        print "Extraction des intersections des polygones a l'aide d'un arbre de decision..."

class ComboBoxClass1(object):
    """Implementation for addin_addin.combobox (ComboBox)"""
    def __init__(self):
        self.items = ["Vegetation saine", "Vegetation fletrie", "Sable sec", "Sable humide", "Laisse de mer"]
        self.editable = True
        self.enabled = False
        self.dropdownWidth = 'WWWWWWWWWWWWWW'
        self.width = 'WWWWWWWWWWWWWW'
    def onSelChange(self, selection):
        global selectedClass
        selectedClass = selection
    def onEditChange(self, text):
        pass
    def onFocus(self, focused):
        pass
    def onEnter(self):
        pass
    def refresh(self):
        pass