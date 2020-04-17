import os
import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import configparser

Config = configparser.ConfigParser()
Config.read("./encryptBook_App/data/config.ini")

class mainView(Gtk.ApplicationWindow):
    def init(self):
        #runs when class is instanciated
        builder = Gtk.Builder()
        builder.add_from_file("data/app_view.glade")
        builder.connect_signals(Handler())

        window = builder.get_object("window1")
        window.show_all()

        Gtk.main()
    
class Handler():
    def onDestroy(self, *args):
        Gtk.main_quit()

    def onButtonPressed(self, button):
        print("Hello World!")