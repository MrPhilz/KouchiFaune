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
        self.enabled = True
        self.dropdownWidth = 'WWWWWWWWWWWWWW'
        self.width = 'WWWWWWWWWWWWWW'
    def onSelChange(self, selection):
        global selectedClass
        selectedClass = selection

class ToolClass48(object):
    """Implementation for addin_addin.tool (Tool)"""
    def __init__(self):
        self.enabled = True
        self.shape = "Line" # Can set to "Line", "Circle" or "Rectangle" for interactive shape drawing and to activate the onLine/Polygon/Circle event sinks.

    def onClick(self):
        layerNames = []
        for layer in arcpy.mapping.ListLayers(arcpy.mapping.MapDocument("CURRENT"), "", None):
            layerNames.append(layer.name)
        if "training_sites" in layerNames:
            print "La couche contenant les sites d'entrainement existe deja!"
        else:
            # Set local variables
            out_path = wdPath
            out_name = "training_sites"
            geometry_type = "POLYGON"
            template = ""
            has_m = "DISABLED"
            has_z = "DISABLED"
            # Use Describe to get a SpatialReference object
            spatial_ref = arcpy.Describe(rasterPath).spatialReference
            # Execute CreateFeatureclass
            self.result = arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, template,
                                                has_m, has_z, spatial_ref)
            arcpy.AddField_management("training_sites", "Classe", "TEXT")

    def onLine(self, line_geometry):
        print "Creation du site d'entrainement..."
        self.site = line_geometry.getPart(0)
        coord = []
        for pt in self.site:
            coord.append([pt.X, pt.Y])

        firstpoint = coord[0]
        coord.append(firstpoint)

        print "Coord avec premier point (pour fermer polygone) ", coord

        global trainingSitesDB
        trainingSitesDB = self.result[0]
        with arcpy.da.InsertCursor(trainingSitesDB, ['SHAPE@']) as cursor:
            cursor.insertRow([coord])
        with arcpy.da.UpdateCursor(trainingSitesDB, ["Classe"]) as cursor:
            for row in cursor:
                if row[0] == u' ':
                    print "list is empty"
                    row[0] = selectedClass
                    cursor.updateRow(row)
                print row

        arcpy.RefreshActiveView()

class ButtonClass4(object):
    """Implementation for addin_addin.button_4 (Button)"""
    def __init__(self):
        self.enabled = False
        self.checked = False
    def onClick(self):
        print "Classification de la couche matricielle..."
        inRaster = ""
        inSamples = ""
        for layer in arcpy.mapping.ListLayers(arcpy.mapping.MapDocument("CURRENT"), "", None):
            if layer.name == "extracted raster":
                inRaster = layer
        for layer in arcpy.mapping.ListLayers(arcpy.mapping.MapDocument("CURRENT"), "", None):
            if layer.name == "training_sites":
                inSamples = layer
        print inRaster, inSamples
        outSig = wdPath+"\sig_file.gsg"
        arcpy.sa.CreateSignatures(inRaster, inSamples, outSig)

        arcpy.sa.MLClassify("extracted raster", outSig, "0.0",
                   "EQUAL", "", wdPath+"\MLClassif")

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
