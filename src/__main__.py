import wx

from ui.mainWindow import Main


class MyApp(wx.App):
    def OnInit(self):
        frame = Main(None, -1, 'toolbar.py')
        frame.Show(True)
        return True

app = MyApp(0)
app.MainLoop()
