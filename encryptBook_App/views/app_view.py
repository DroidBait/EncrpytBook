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
    box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
    self.add(box_outer)

    listbox = Gtk.ListBox()
    listbox.set_selection_mode(Gtk.SelectionMode.NONE)
    box_outer.pack_start(listbox, True, True, 0)

    #get list of users from the entities json file
    entities = import_entities()
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
    
    #listbox.set_property("width-request", 100)
    listbox.set_size_request(100,100)
    

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

def listbox_edit(self):
    #will show details of each enitity when selected from previous listbox
    editList = Gtk.ListBox()
    editList.set_selection_mode(Gtk.SelectionMode.NONE)
