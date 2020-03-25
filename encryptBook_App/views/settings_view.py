import os
import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class settings_page(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="EncrpytBook Settings")
        self.set_default_size(300, 200)
        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box_outer)

        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        box_outer.pack_start(listbox, True, True, 0)

        orderByRow = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        orderByRow.add(hbox)
        label = Gtk.Label("Order by:", xalign=0)
        orderByCombo = Gtk.ComboBoxText()
        orderByCombo.insert(0, "0", "First Name")
        orderByCombo.insert(1, "1", "Last Name")
        orderByCombo.set_active(0)
        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(orderByCombo, False, True, 0)
        listbox.add(orderByRow)

