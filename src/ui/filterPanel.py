import wx


class FilterPanel(wx.Panel):
    def __init__(self, parent, ID, filter_string=None):
        wx.Panel.__init__(self, parent, ID, wx.DefaultPosition)
        self.filter_string = filter_string
