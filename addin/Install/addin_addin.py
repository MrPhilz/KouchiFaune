# -*- coding: utf-8 -*-

import arcpy
import pythonaddins

arcpy.env.overwriteOutput = True

class ButtonClass1(object):
    """Implementation for addin_addin.button_1 (Button)"""

    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        print "Choix d'un repertoire de travail, ainsi que l'image a classifier..."
        global wdPath
        wdPath = pythonaddins.OpenDialog("Selectionnez un repertoire de travail...", False, "C:", "Ajouter")
        print wdPath
        global rasterPath
        rasterPath = pythonaddins.OpenDialog("Selectionnez une couche matricielle...", False, "C:", "Ajouter")
        print rasterPath

        arcpy.MakeRasterLayer_management(rasterPath, "rasterLayer")

class ToolClass41(object):
    """Implementation for addin_addin.tool (Tool)"""
    def __init__(self):
        self.enabled = True
        self.cursor = 3
        self.shape = "Line" # Can set to "Line", "Circle" or "Rectangle" for interactive shape drawing and to activate the onLine/Polygon/Circle event sinks.

    def onLine(self, line_geometry):
        print "Creation du masque..."
        self.maskPart = line_geometry.getPart(0)
        coord = []
        for pt in self.maskPart:
            coord.append([pt.X, pt.Y])

        firstpoint = coord[0]
        coord.append(firstpoint)

        print "Coord avec premier point (pour fermer polygon) ", coord

        # Set local variables
        out_path = wdPath
        out_name = "maskRaster"
        geometry_type = "POLYGON"
        template = ""
        has_m = "DISABLED"
        has_z = "DISABLED"
        # Use Describe to get a SpatialReference object
        spatial_ref = arcpy.Describe(rasterPath).spatialReference
        # Execute CreateFeatureclass
        result = arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, template,
                                            has_m, has_z, spatial_ref)

        global mask_class
        mask_class = result[0]
        with arcpy.da.InsertCursor(mask_class, ['SHAPE@']) as cursor:
            cursor.insertRow([coord])

class ToolClass43(object):
    """Implementation for addin_addin.tool_2 (Tool)"""
    def __init__(self):
        self.enabled = True
        self.shape = "NONE" # Can set to "Line", "Circle" or "Rectangle" for interactive shape drawing and to activate the onLine/Polygon/Circle event sinks.
    def onClick(self):
        print "Execution du Extract by Mask..."
        # Set local variables
        inRaster = rasterPath
        inMaskData = mask_class

        # Execute ExtractByMask
        outExtractByMask = arcpy.sa.ExtractByMask(inRaster, inMaskData)
        arcpy.MakeRasterLayer_management(outExtractByMask, "extracted raster")

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
