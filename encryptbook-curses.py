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
    startList = 0
    endList = 1
    entryMode = 'exit'
    entryStep = 'step1'

    ##############################
    ## Generate the two windows ##
    ##############################
    contactPadPos = 0
    listLength = printMainView(stdscr, scrWidth, currentRow, contactPadPos, startList, endList, entryMode, entryStep)
    #time.sleep(3) #hopefully will be deprecated soon
    lengthEntitiesList = listLength
    if listLength > scrWidth.gety() - 7:
        listLength = scrWidth.gety() - 7
    endList = listLength


    while 1:
        key = stdscr.getch()

        if key == curses.KEY_UP and currentRow > 0:
            currentRow -= 1
            if currentRow == startList and startList > 0:
                startList -= 1
                endList -= 1
        elif key == curses.KEY_DOWN and currentRow < listLength - 1:
            currentRow += 1
            if currentRow == listLength - 1 and endList <= lengthEntitiesList: #pass back the length of the entities list
                startList += 1
                endList += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            #print_center(stdscr, "You selected '{}'".format(menu[current_row]))
            tmp = 1
            tmp += 1
            # if user selected last row, exit the program
            #if currentRow == len(menu)-1:
                #break
        elif key == ord('q'):
            break
        elif key == ord('a'):
            entryMode = 'add'

        listLength = printMainView(stdscr, scrWidth, currentRow, contactPadPos, startList, endList, entryMode, entryStep)

def printMainView(stdscr, scrWidth, currentRow, contactPadPos, startList, endList, entryMode, entryStep):
    ##############################
    ## Generate the two windows ##
    ##############################
    list1, listLength, selectedContact = list_view(scrWidth, currentRow, startList, endList) #get the list of known contacts
    contact = contact_view(scrWidth, selectedContact) #get the contact view which displays info about thu contacts
    #contact = contact_view(scrWidth, selectedContact)
    bottomBar = printBottomBar(scrWidth, entryMode, entryStep)
    list1.refresh() # display the list
    #contact.refresh(contactPadPos, 0, 0, scrWidth.getx25() + 1, scrWidth.gety() - 5, scrWidth.getx75()) #display the contact info
    contact.refresh()
    bottomBar.refresh()
    return listLength

def list_view(scrWidth, currentRow, startList, endList):
    listWindow = curses.newwin(scrWidth.gety() - 5, scrWidth.getx25(), 0, 0)
    #listWindow.addstr(5, 2, "hello world")
    listWindow.border(1)
    listLength, selectedContact = printList(listWindow, currentRow, startList, endList)
    return listWindow, listLength, selectedContact

def printList(listWindow, currentSelectedRow, startList, endList): #will need to return the data of the seleted row
    entities = import_entities()
    #sort the list
    if Config.get('SETTINGS', 'alphabetically_sort') == 'ascending':
        entities.sort(reverse=False)
    elif Config.get('SETTINGS', 'alphabetically_sort') == 'descending':
        entities.sort(reverse=True)
    else:
        entities.sort(reverse=False)
    loopNum = 0
    selectedContact = ""

    for idx, row in enumerate(entities):
        if idx >= startList and idx < endList:
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
    contWindow = curses.newwin(scrWidth.gety() - 5, scrWidth.getx75(), 0, scrWidth.getx25())
    #contWindow = curses.newpad(scrWidth.gety() - 4, scrWidth.getx75())
    contWindow.border(1)
    #contWindow.addstr(5, 5, "contact view")
    #contWindow.addstr(6, 5, str(scrWidth.getx25()))
    with open("./data/entities.json", "r") as file:
        contacts = json.load(file)
        for doc in contacts['entities']:
            first = doc['first']
            middle = doc['middle']
            last = doc['last']
            sortFirst = "" + first + " " + middle + " " + last
            sortLast = last + ", " + first + " " + middle
            if selectedContact == sortFirst or selectedContact == sortLast:
                #print the data to the screen for viewing
                contWindow.addstr(1, 1, "First Name: " + doc['first'])
                contWindow.addstr(2, 1, "Middle Name: " + doc['middle'])
                contWindow.addstr(3, 1, "Last Name: " + doc['last'])
                contWindow.addstr(4, 1, "Home Phone: " + doc['homePhone'])
                contWindow.addstr(5, 1, "Mobile Phone: " + doc['mobilePhone'])
                contWindow.addstr(6, 1, "Address Line 1: " + doc['address1'])
                contWindow.addstr(7, 1, "Address Line 2: " + doc['address2'])
                contWindow.addstr(8, 1, "Address Line 3: " + doc['address3'])
                contWindow.addstr(9, 1, "Postcode: " + doc['postcode'])
                contWindow.addstr(10, 1, "Nickname: " + doc['nickname'])
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

def printBottomBar(scrWidth, entryMode, entryStep):
    bar = curses.newwin(4, scrWidth.getx(), scrWidth.gety() - 4, 0)
    bar.border(1)
    if entryMode == 'exit':
        bar.addstr(1, 1, "a: add")
        bar.addstr(2, 1, "e: edit")
    if entryMode != 'exit':
        #if entryStep == 'step1':
        #    bar.addstr(1, 1, 'Enter First Name:')
        #    curses.echo()
        #    fName = bar.getstr(2, 1, 20)
        #    curses.noecho()
        #    curses.cbreak()
        #    bar.keypad(True)
        #    entryStep = 'step2'
        #elif entryStep == 'step2':
        #    bar.addstr(1, 1, 'Enter Middle Name:')
        bar.addstr(1,1, 'test 1111')
        curses.echo()
        ss = bar.getstr(2, 1, 20)
        #curses.cbreak()
        bar.keypad(1)
        bar.refresh()
        bar.addstr(1,1, 'test 2222')
        bar.addstr(2,1,'')
        sss = bar.getstr(2,1, 20)
        bar.keypad(1)
        bar.refresh()
        curses.noecho()
        entryMode = 'start'
        bar.refresh()

    return bar

curses.wrapper(main)
