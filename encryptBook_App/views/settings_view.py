import os
import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import configparser

Config = configparser.ConfigParser()
Config.read("./encryptBook_App/data/config.ini")

global sortValue
global orderByValue

class settings_page(Gtk.Window):


    def __init__(self):
        ####################
        ## Create window  ##
        ## Create listbox ##
        ####################
        Gtk.Window.__init__(self, title="EncrpytBook Settings")
        self.set_default_size(300, 200)
        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box_outer)

        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        box_outer.pack_start(listbox, True, True, 0)

        #############################
        ## Add order by to listbox ##
        #############################
        orderByRow = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        orderByRow.add(hbox)
        label = Gtk.Label("Order by:", xalign=0)
        global orderByCombo
        orderByCombo = Gtk.ComboBoxText()
        orderByCombo.insert(0, "0", "First Name")
        orderByCombo.insert(1, "1", "Last Name")
        if Config.get('SETTINGS', 'order_by') == 'last':
            orderByCombo.set_active(1)
        elif Config.get('SETTINGS', 'order_by') == 'first':
            orderByCombo.set_active(0)
        else:
            print("Error reading order by setting")
            orderByCombo.set_active(0)
        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(orderByCombo, False, True, 0)
        listbox.add(orderByRow)

        ############################
        ## Add sort by to listbox ##
        ############################
        hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        ascDesRow = Gtk.ListBoxRow()
        ascDesRow.add(hbox2)
        labelSort = Gtk.Label("Sort:", xalign=0)
        global sortCombo
        sortCombo = Gtk.ComboBoxText()
        sortCombo.insert(0, "0", "Ascending")
        sortCombo.insert(1, "1", "Descending")
        if Config.get('SETTINGS', 'alphabetically_sort') == 'ascending':
            sortCombo.set_active(0)
        elif Config.get('SETTINGS', 'alphabetically_sort') == 'decsending':
            sortCombo.set_active(1)
        else:
            print("Error reading alphabetically sort")
            sortCombo.set_active(0)
        hbox2.pack_start(labelSort, True, True, 0)
        hbox2.pack_start(sortCombo, False, False, 0)
        listbox.add(ascDesRow)

        ################################
        ## Add save button to listbox ##
        ################################
        saveRow = Gtk.ListBoxRow()
        saveButton = Gtk.Button.new_with_label("Save")
        saveButton.connect("clicked", self.on_save_clicked)
        saveRow.add(saveButton)
        listbox.add(saveRow)

    ###################################
    ## Runs when save button clicked ##
    ###################################
    def on_save_clicked(self, button):
        print("\"save\" was clicked")
        self.saveChangesToFile()
    
    def saveChangesToFile(self):
        config = configparser.RawConfigParser()
        with open("./encryptBook_App/data/config.ini", "w") as configfile:
            config.add_section('SETTINGS')

            ##############
            ## order by ##
            ##############
            print("Order by set to; ", orderByCombo.get_active_text())
            if orderByCombo.get_active_text() == "Last Name":
                config.set('SETTINGS', 'order_by', 'last')
            elif orderByCombo.get_active_text() == "First Name":
                config.set('SETTINGS', 'order_by', 'first')
            else:
                print("Error in setting order by. Setting to default: Last Name")
                config.set('SETTINGS', 'order_by', 'last')
            
            #########################
            ## Alphabetically sort ##
            #########################
            print('Alphabetically sort set to: ', sortCombo.get_active_text())
            if sortCombo.get_active_text() == "Ascending":
                config.set('SETTINGS', 'alphabetically_sort', 'ascending')
            elif sortCombo.get_active_text() ==  "Descending":
                config.set('SETTINGS', 'alphabetically_sort', 'descending')
            else:
                print("Error in setting alphabetically by. Returning to default: Ascending")
                config.set('SETTINGS', 'alphabetically_sort', 'ascending')
            
            #####################
            ## write to config ##
            #####################
            config.write(configfile)
    