import os
import sys
import configparser
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import json

Config = configparser.ConfigParser()
Config.read("./encryptBook_App/data/config.ini")

def listbox_entities(self):
    #Gtk.Window.__init__(self, title="EncrpytBook")
    #self.set_border_width(3)

    box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
    self.add(box_outer)

    listbox = Gtk.ListBox()
    listbox.set_selection_mode(Gtk.SelectionMode.NONE)
    box_outer.pack_start(listbox, True, True, 0)

    #get list of users from the entities json file
    entities = import_entities();
    #sort the list
    if Config.get('SETTINGS', 'alphabetically_sort') == 'ascending':
        entities.sort(reverse=False)
    elif Config.get('SETTINGS', 'alphabetically_sort') == 'descending':
        entities.sort(reverse=True)
    else:
        entities.sort(reverse=False)
    for item in entities:
        row = Gtk.ListBoxRow()
        row.add(Gtk.Label(item, xalign=0))
        listbox.add(row)

def import_entities():
    # import from file
    lists = []
    with open("./encryptBook_App/data/entities.json", "r") as jsonFile:
        data = json.load(jsonFile)
        for doc in data['entities']:
            first = doc['first']
            middle = doc['middle']
            last = doc['last']
            if Config.get('SETTINGS', 'order_by') == 'last':
                lists.append(last + ", " + first + " " + middle)
            elif Config.get('SETTINGS', 'order_by') == 'first':
                lists.append(first + ' ' + middle + ' ' + last)
            else:
                lists.append(last + "," + first + " " + middle)
    return lists
