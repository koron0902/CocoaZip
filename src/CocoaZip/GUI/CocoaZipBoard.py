import wx
import os
from .mainWindow import mainWindow
 
class CocoaZipBoard(wx.App):
    def OnInit(self):
        frame = mainWindow(None, -1, "CocoaZip", (1000, 500))
        frame.Show()
        #self.createMenu()
        #self.createList()
        #self.frm_main.Show()
        return True
 