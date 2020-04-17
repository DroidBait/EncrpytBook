import os
import sys
import curses
import time

def main(stdscr):
    #Set up the curses environment
    #remove the blinking cursor
    curses.curs_set(0)
    list1 = list_view() #get the list of known contacts
    contact = contact_view() #get the contact view which displays info about thu contacts
    list1.refresh() # display the list
    contact.refresh() #display the contact info
    time.sleep(3) #hopefully will be deprecated soon
    #stdscr.refresh()
    #time.sleep(3)

def list_view():
    listWindow = curses.newwin(20, 10, 0, 0)
    listWindow.addstr(5, 2, "hello world")
    listWindow.border(1)
    return listWindow

def contact_view():
    contWindow = curses.newwin(20, 10, 0, 25)
    contWindow.border(1)
    contWindow.addstr(5, 2, "contact view")
    return contWindow


curses.wrapper(main)
