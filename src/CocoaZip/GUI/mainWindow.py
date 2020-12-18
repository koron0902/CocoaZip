import wx
import os
 
class mainWindow(wx.Frame):
    def __init__(self, parent, id, title, size):
        wx.Frame.__init__(self, parent, id, title = title, size = size, style = wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)
        self.MainLayout = wx.BoxSizer(wx.HORIZONTAL)
        self.LeftBox = wx.BoxSizer(wx.VERTICAL)
        self.RightBox = wx.BoxSizer(wx.VERTICAL)
        self.panel = wx.Panel(self, wx.ID_ANY)
        self.panel.SetBackgroundColour('#FFFFFF')


        self.createMenu()
        self.RightBox.Add(self.createEncryption())
        self.RightBox.Add(self.createList(), wx.EXPAND, flag = wx.EXPAND)
        self.RightBox.Add(self.createButton(), flag = wx.EXPAND)
        self.RightBox.Add(self.createOutput(), flag = wx.EXPAND)
        self.MainLayout.Add(self.RightBox, wx.EXPAND, wx.EXPAND)
        self.SetSizer(self.MainLayout)
 
 
    def createMenu(self):
        fileMenu = wx.Menu()
        open = fileMenu.Append(-1, "&Open")
        save = fileMenu.Append(-1, "&Save")
        exit = fileMenu.Append(-1, "&Exit")
 
        self.Bind(wx.EVT_MENU, self.OnOpen, open)
        self.Bind(wx.EVT_MENU, self.OnSave, save)
        self.Bind(wx.EVT_MENU, self.OnExit, exit)
 
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        self.SetMenuBar(menuBar)

    def createEncryption(self):
        def generation(event):
            self.password.SetValue("afeafaef")

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
        pwSizer = wx.BoxSizer(wx.HORIZONTAL)
        encryption = wx.CheckBox(self.panel, wx.ID_ANY, '暗号化する')
        visible = wx.CheckBox(self.panel, wx.ID_ANY, 'パスワードを表示する')
        generate = wx.Button(self.panel, label="パスワードの生成")
        self.password = wx.TextCtrl(self.panel)
        generate.Bind(wx.EVT_BUTTON, generation)
        buttonSizer.Add(encryption)
        buttonSizer.Add(visible)
        pwSizer.Add(self.password)
        pwSizer.Add(generate)
        mainSizer.Add(buttonSizer)
        mainSizer.Add(pwSizer, flag = wx.EXPAND)

        return mainSizer

    def createOutput(self):
        def selectFolder(event):
            filter = "zip file(*.zip)|*.zip|All file(*.*)|*.*"
            path = os.path.dirname(__file__)
            dialog = wx.FileDialog(None, u'ファイルを選択してください', '', '', filter, style = wx.FD_SAVE)
    
            if dialog.ShowModal() == wx.ID_OK:
                dir = dialog.GetDirectory()
                file = dialog.GetFilename()
                print(os.path.join(dir, file))

            dialog.Destroy()

        Button = wx.Button(self.panel, label="Archive")
        Button.Bind(wx.EVT_BUTTON, selectFolder)

        return Button


    def createButton(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.selectFolderButton = wx.Button(self.panel, label="Add Folder")
        self.selectFileButton = wx.Button(self.panel, label="Add File")
        self.selectFolderButton.Bind(wx.EVT_BUTTON, self.onSelectFolder)
        self.selectFileButton.Bind(wx.EVT_BUTTON, self.onSelectFile)
        sizer.Add(self.selectFileButton, wx.EXPAND, wx.EXPAND)
        sizer.Add(self.selectFolderButton, wx.EXPAND, wx.EXPAND)
        return sizer
    
    def onSelectFolder(self, event):
        path = os.path.dirname(__file__)
        dialog = wx.DirDialog(self, u'フォルダを選択してください', path, wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
 
        if dialog.ShowModal() == wx.ID_OK:
            self.CompressTarget.Append(dialog.GetPath(), dialog.GetPath())

        dialog.Destroy()

    def onSelectFile(self, event):
        filter = "All file(*.*)|*.*"
        path = os.path.dirname(__file__)
        dialog = wx.FileDialog(self, u'ファイルを選択してください', path, '', filter, wx.FD_OPEN)
 
        if dialog.ShowModal() == wx.ID_OK:
            dir = dialog.GetDirectory()
            file = dialog.GetFilename()
            self.CompressTarget.Append(os.path.join(dir, file), os.path.join(dir, file))
        dialog.Destroy()


    def createList(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        label = wx.StaticText(self.panel, -1, "圧縮対象", style = wx.ALIGN_CENTER | wx.DOUBLE_BORDER)
        self.CompressTarget = wx.ListBox(self, wx.ID_ANY, style = wx.DOUBLE_BORDER)
        sizer.Add(label, flag = wx.EXPAND, border = 10)
        sizer.Add(self.CompressTarget, wx.EXPAND, wx.EXPAND)

        return sizer
 

    def OnOpen(self, evvent):
        filter = "csv file(*.csv)|*.csv|All file(*.*)|*.*"
        path = os.path.dirname(__file__)
        dialog = wx.FileDialog(self, u'ファイルを選択してください', path, '', filter, wx.FD_OPEN)
 
        if dialog.ShowModal() == wx.ID_OK:
            dir = dialog.GetDirectory()
            file = dialog.GetFilename()
        dialog.Destroy()
 
        print(os.path.join(dir, file))
 
        self.canvas.ReadFromCSV(os.path.join(dir, file))
 
    def OnSave(self, event):
        pass
 
    def OnExit(self, event):
        self.frm_main.Close()