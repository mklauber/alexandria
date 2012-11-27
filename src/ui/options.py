import wx

import __preferences__ as preferences
prefs = preferences.load_preferences()


class OptionsDialog(wx.Dialog):
    """Options dialog for managing user exposed options."""

    def __init__(self, parent, id, title):
        pref_layout = prefs['optionsLayout']
        size = wx.Size(pref_layout['width'], pref_layout['height'])
        wx.Dialog.__init__(self, parent, id, title, wx.DefaultPosition, size)
        nb = wx.Notebook(self)

        nb.AddPage(GeneralPanel(nb), "General")
        nb.AddPage(LensPanel(nb), "lenses")


class GeneralPanel(wx.Panel):
    pass


class LensPanel(wx.Panel):
    pass
