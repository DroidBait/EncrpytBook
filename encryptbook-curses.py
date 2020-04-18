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
    ###################################
    ## Set up the curses environment ##
    ## remove the blinking cursor    ##
    ###################################
    h, w = stdscr.getmaxyx()
    scrWidth = tp(w, h)
    curses.curs_set(0)
    currentRow = 0
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    ##############################
    ## Generate the two windows ##
    ##############################
    # list1 = list_view(scrWidth, currentRow) #get the list of known contacts
    # contact = contact_view(scrWidth) #get the contact view which displays info about thu contacts
    # list1.refresh() # display the list
    # contact.refresh() #display the contact info
    printMainView(stdscr, scrWidth, currentRow)
    time.sleep(3) #hopefully will be deprecated soon
    #while 1:
    #    key = stdscr.getch()

    #    if key == curses.KEY_UP and current_row > 0:
    #        current_row -= 1
    #    elif key == curses.KEY_DOWN and current_row < len(menu)-1:
    #        current_row += 1
    #    elif key == curses.KEY_ENTER or key in [10, 13]:
    #        print_center(stdscr, "You selected '{}'".format(menu[current_row]))
    #        stdscr.getch()
    #        # if user selected last row, exit the program
    #        if current_row == len(menu)-1:
    #            break

    #    print_menu(stdscr, current_row)

def printMainView(stdscr, scrWidth, currentRow,):
    ##############################
    ## Generate the two windows ##
    ##############################
    list1 = list_view(scrWidth, currentRow) #get the list of known contacts
    contact = contact_view(scrWidth) #get the contact view which displays info about thu contacts
    list1.refresh() # display the list
    contact.refresh() #display the contact info

def list_view(scrWidth, currentRow):
    listWindow = curses.newwin(scrWidth.gety(), scrWidth.getx25(), 0, 0)
    #listWindow.addstr(5, 2, "hello world")
    listWindow.border(1)
    printList(listWindow, currentRow)
    return listWindow

def printList(listWindow, currentSelectedRow): #will need to return the data of the seleted row
    entities = import_entities()
    #sort the list
    if Config.get('SETTINGS', 'alphabetically_sort') == 'ascending':
        entities.sort(reverse=False)
    elif Config.get('SETTINGS', 'alphabetically_sort') == 'descending':
        entities.sort(reverse=True)
    else:
        entities.sort(reverse=False)
    loopNum = 0
    #for item in entities:
    #    listWindow.addstr(loopNum + 1, 0, item)
    #    loopNum += 1
    for idx, row in enumerate(entities):
        if idx == currentSelectedRow:
            listWindow.attron(curses.color_pair(1))
            listWindow.addstr(loopNum + 1, 0, row)
            listWindow.attroff(curses.color_pair(1))
            #todo
            #create some variables
            #returns the first, last & middle name of selected row
        else:
            listWindow.addstr(loopNum + 1, 0, row)
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
