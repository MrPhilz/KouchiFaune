#-*- coding: utf-8 -*-
import arcpy
import pythonaddins

class ButtonClass1(object):
    """Implementation for addin_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClass2(object):
    """Implementation for addin_addin.button_1 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClass3(object):
    """Implementation for addin_addin.button_2 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClass4(object):
    """Implementation for addin_addin.button_3 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClass5(object):
    """Implementation for addin_addin.button_4 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ComboBoxClass1(object):
    """Implementation for addin_addin.combobox (ComboBox)"""
    def __init__(self):
        self.items = ["Vegetation saine", "Vegetation fletrie", "Sable sec", "Sable humide", "Laisse de mer"]
        self.editable = True
        self.enabled = True
        self.dropdownWidth = 'WWWWWWWWWWWWWW'
        self.width = 'WWWWWWWWWWWWWW'
    def onSelChange(self, selection):
        pass
    def onEditChange(self, text):
        pass
    def onFocus(self, focused):
        pass
    def onEnter(self):
        pass
    def refresh(self):
        pass