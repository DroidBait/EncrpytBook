import os
import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class settings_page(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="EncrpytBook Settings")
        self.set_default_size(300, 200)
        
