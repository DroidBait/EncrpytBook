import os
import sys
import curses
import time
import json
from classes.dimension import tuplexy as tp
import configparser

Config = configparser.ConfigParser()
Config.read("./data/config.ini")

def main(stdscr):
    #Set up the curses environment
    #remove the blinking cursor
    h, w = stdscr.getmaxyx()
    scrWidth = tp(w, h)
    curses.curs_set(0)
    list1 = list_view(scrWidth) #get the list of known contacts
    contact = contact_view(scrWidth) #get the contact view which displays info about thu contacts
    list1.refresh() # display the list
    contact.refresh() #display the contact info
    time.sleep(3) #hopefully will be deprecated soon


def list_view(scrWidth):
    listWindow = curses.newwin(scrWidth.gety(), scrWidth.getx25(), 0, 0)
    #listWindow.addstr(5, 2, "hello world")
    listWindow.border(1)
    entities = import_entities()
    #sort the list
    if Config.get('SETTINGS', 'alphabetically_sort') == 'ascending':
        entities.sort(reverse=False)
    elif Config.get('SETTINGS', 'alphabetically_sort') == 'descending':
        entities.sort(reverse=True)
    else:
        entities.sort(reverse=False)
    loopNum = 0
    for item in entities:
        #row = Gtk.ListBoxRow()
        #row.add(Gtk.Label(item, xalign=0))
        #listbox.add(row)
        listWindow.addstr(loopNum + 1, 0, item)
        loopNum += 1
    return listWindow

def contact_view(scrWidth):
    contWindow = curses.newwin(scrWidth.gety(), scrWidth.getx75(), 0, scrWidth.getx25())
    contWindow.border(1)
    contWindow.addstr(5, 5, "contact view")
    contWindow.addstr(6, 5, str(scrWidth.getx25()))
    return contWindow

def import_entities():
    # import from file
    lists = []
    with open("./data/entities.json", "r") as jsonFile:
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

curses.wrapper(main)
