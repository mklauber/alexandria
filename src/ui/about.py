import wx
from __strings__ import get_local_strings
locale = get_local_strings()


class AboutDialog(wx.Dialog):
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title, wx.DefaultPosition,
                           wx.Size(300, 300))
        panel = wx.Panel(self, -1)

        # Application Name
        name = wx.StaticText(panel, -1, locale['appName'],
                    (100, 25), style=wx.ALIGN_CENTRE)
        name.SetFont(wx.Font(14, wx.NORMAL, wx.BOLD, wx.NORMAL))
        wx.StaticText(panel, -1, "Version: %s" % locale['appVersion'],
                      (100, 45))

        description = wx.StaticText(panel, -1, locale['appDescription'],
                    (25, 100), style=wx.ALIGN_CENTRE)
        description.SetFont(wx.Font(10, wx.NORMAL, wx.ITALIC, wx.NORMAL))
        description.Wrap(250)

        name = wx.StaticText(panel, -1,
            "Author(s): %s" % '\n'.join(locale['appAuthors']),
            (50, 200), style=wx.ALIGN_CENTRE)
        name.SetFont(wx.Font(10, wx.NORMAL, wx.NORMAL, wx.NORMAL))

        self.Center()
