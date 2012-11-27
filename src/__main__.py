import wx

from ui.mainWindow import MyMenu


class MyApp(wx.App):
    def OnInit(self):
        frame = MyMenu(None, -1, 'toolbar.py')
        frame.Show(True)
        return True

app = MyApp(0)
app.MainLoop()
