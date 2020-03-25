import os
import sys
import configparser
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
from views.app_view import listbox_entities


class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="EncryptBook", application=app)
        self.set_default_size(200, 200)
        listbox_entities(self)

class MyApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

        # a builder to add the UI designed with Glade to the grid:
        builder = Gtk.Builder()
        # get the file (if it is there)
        try:
            builder.add_from_file("encryptBook_App/data/menubar.ui")
        except:
            print("file not found")
            sys.exit()

        # we use the method Gtk.Application.set_menubar(menubar) to add the menubar
        # to the application (Note: NOT the window!)
        self.set_menubar(builder.get_object("menubar"))

        # action without a state created (name, parameter type)
        quit_action = Gio.SimpleAction.new("quit", None)
        # connected with the callback function
        quit_action.connect("activate", self.quit_callback)
        # added to the window
        self.add_action(quit_action)
    
    # callback function for copy_action
    def quit_callback(self, action, parameter):
        print("\"Quit\" activated")
        sys.exit()

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)

#win = MyWindow()
#win.connect("destroy", Gtk.main_quit)
#win.show_all()
#Gtk.main()