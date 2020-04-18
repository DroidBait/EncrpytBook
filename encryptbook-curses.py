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
    listLength = printMainView(stdscr, scrWidth, currentRow)
    #time.sleep(3) #hopefully will be deprecated soon
    while 1:
        key = stdscr.getch()

        if key == curses.KEY_UP and currentRow > 0:
            currentRow -= 1
        elif key == curses.KEY_DOWN and currentRow < listLength-1:
            currentRow += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            #print_center(stdscr, "You selected '{}'".format(menu[current_row]))
            tmp = 1
            tmp += 1
            # if user selected last row, exit the program
            #if currentRow == len(menu)-1:
                #break

        listLength = printMainView(stdscr, scrWidth, currentRow)

def printMainView(stdscr, scrWidth, currentRow,):
    ##############################
    ## Generate the two windows ##
    ##############################
    list1, listLength, selectedContact = list_view(scrWidth, currentRow) #get the list of known contacts
    contact = contact_view(scrWidth, selectedContact) #get the contact view which displays info about thu contacts
    list1.refresh() # display the list
    contact.refresh() #display the contact info
    return listLength, selectedContact

def list_view(scrWidth, currentRow):
    listWindow = curses.newwin(scrWidth.gety(), scrWidth.getx25(), 0, 0)
    #listWindow.addstr(5, 2, "hello world")
    listWindow.border(1)
    listLength, selectedContact = printList(listWindow, currentRow)
    return listWindow, listLength, selectedContact

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
    
    for idx, row in enumerate(entities):
        if idx == currentSelectedRow:
            listWindow.attron(curses.color_pair(1))
            listWindow.addstr(loopNum + 1, 0, row)
            listWindow.attroff(curses.color_pair(1))
            #todo
            #create some variables
            #returns the first, last & middle name of selected row
            selectedContact = row
        else:
            listWindow.addstr(loopNum + 1, 0, row)
        loopNum += 1
    return len(entities), selectedContact

def contact_view(scrWidth, selectedContact):
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
