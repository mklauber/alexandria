import wx

from about import AboutDialog
from options import OptionsDialog

import __preferences__ as preferences
prefs = preferences.load_preferences()


class Main(wx.Frame):
    """Main window for browsing and filtering files."""

    def __init__(self, parent, id, title):
        pref_layout = prefs['mainLayout']
        size = wx.Size(pref_layout['width'], pref_layout['height'])
        wx.Frame.__init__(self, parent, id, title,
            wx.DefaultPosition, size)
        # Save the window size for next use.
        self.Bind(wx.EVT_SIZE, self.save_layout_preferences, self)
        self.CreateStatusBar()

        # Menu bar
        menubar = wx.MenuBar()
        self.SetMenuBar(menubar)

        # Top level Menus
        file = wx.Menu()
        menubar.Append(file, '&File')
        help = wx.Menu()
        menubar.Append(help, '&Help')

        # File Menu Items
        options = file.Append(wx.ID_PREFERENCES, "&Options", "Program Options")
        self.Bind(wx.EVT_MENU, self.on_options, options)
        # Seperator before quit
        file.AppendSeparator()
        close = file.Append(wx.ID_EXIT, "E&xit", " Terminate the program")
        self.Bind(wx.EVT_MENU, self.on_close, close)

        # Help Menu Items
        about = help.Append(wx.ID_ABOUT, "&About", "About alexandria")
        self.Bind(wx.EVT_MENU, self.on_about, about)

        # Layout of main panel

        # Filter string row
        display = wx.TextCtrl(self, -1, '', style=wx.TE_RIGHT)
        clear_filter = wx.Button(self, -1, "Clear")
        run_filter = wx.Button(self, -1, "Run")

        splitter = wx.SplitterWindow(self, -1)
        # Splitter subpanels
        left = wx.Panel(splitter, wx.EXPAND)
        self.nb = wx.Notebook(splitter)

        # Splitter Window for filters
        splitter.SplitVertically(left, self.nb)
        splitter.SetSashGravity(0)
        splitter.SetMinimumPaneSize(50)
        splitter.SetSashPosition(pref_layout['dividerPosition'])
        self.Bind(wx.EVT_SPLITTER_SASH_POS_CHANGED,
                  self.save_layout_preferences, splitter)

        # Notebook pages for various
        self.nb.AddPage(FilterPanel(self.nb, wx.EXPAND), "All Files")
        pages = [('Images', None), ('Videos', None), ("Text Documents", None)]
        for title, filter_string in pages:
            panel = FilterPanel(self.nb, wx.EXPAND, filter_string=filter_string)
            self.nb.AddPage(panel, title)


        # Place items in Grid
        sizer = wx.GridBagSizer(2, 2)
        sizer.Add(clear_filter, (0, 0), wx.DefaultSpan)
        sizer.Add(run_filter, (0, 3), wx.DefaultSpan)
        sizer.Add(display, (0, 1), (1, 1), wx.EXPAND)
        sizer.Add(splitter, (1, 0), (1, 4), wx.EXPAND)
        sizer.AddGrowableCol(1)
        sizer.AddGrowableRow(1)

        self.SetSizer(sizer)
        self.Centre()

    def update_tabs(self, pages):
        """Update the existing tabs, changing their filter strings or creating
them if they do not exist."""
        for title, filter_string in pages:
            self.nb.AddPage()

    def on_about(self, event):
        """Show the about box"""
        dlg = AboutDialog(self, -1, "About")
        dlg.ShowModal()
        dlg.Destroy()

    def on_options(self, event):
        """Show the options dialog"""
        dlg = OptionsDialog(self, -1, "Options")
        dlg.ShowModal()
        dlg.Destroy()

    def on_close(self, event):
        self.Close()

    def save_layout_preferences(self, event):
        """Save the splitter sash position to preferences file."""
        pass
        # Include conditional logic to check if maximized.


class FilterPanel(wx.Panel):
    def __init__(self, parent, ID, filter_string=None):
        wx.Panel.__init__(self, parent, ID, wx.DefaultPosition)
        self.filter_string = filter_string
