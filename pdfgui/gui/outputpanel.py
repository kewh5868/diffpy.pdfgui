#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# generated by wxGlade 0.4.1 on Sun Dec  3 17:38:14 2006

import wx
from pdfpanel import PDFPanel

class OutputPanel(wx.Panel,PDFPanel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: OutputPanel.__init__
        kwds["style"] = wx.RAISED_BORDER|wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.headerLabel = wx.StaticText(self, -1, "PDFFit2 Engine Output")
        self.outputCtrl = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL|wx.TE_LINEWRAP)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: OutputPanel.__set_properties
        self.headerLabel.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: OutputPanel.__do_layout
        rootSizer = wx.BoxSizer(wx.VERTICAL)
        rootSizer.Add(self.headerLabel, 0, wx.ADJUST_MINSIZE, 0)
        rootSizer.Add(self.outputCtrl, 1, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        self.SetAutoLayout(True)
        self.SetSizer(rootSizer)
        rootSizer.Fit(self)
        rootSizer.SetSizeHints(self)
        # end wxGlade
        
    def refresh(self):
        pass
        

# end of class OutputPanel

