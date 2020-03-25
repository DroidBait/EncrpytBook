import os
import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class about_page(Gtk.Window):
    def __init__(self):
        about = Gtk.AboutDialog()
        about.set_program_name("EncryptBook")
        about.set_version("0.1")
        about.set_authors("S.Dsn")
        about.set_copyright("(c) S.Dsn")
        about.set_comments("An encrypted address book")
        about.set_website("https://github.com/DroidBait/EncrpytBook")

        about.run()
        about.destroy()
