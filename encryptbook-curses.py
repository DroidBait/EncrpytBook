import os
import sys
import curses
import time
from classes.dimension import tuplexy as tp

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
    listWindow.addstr(5, 2, "hello world")
    listWindow.border(1)
    return listWindow

def contact_view(scrWidth):
    contWindow = curses.newwin(scrWidth.gety(), scrWidth.getx75(), 0, scrWidth.getx25())
    contWindow.border(1)
    contWindow.addstr(5, 5, "contact view")
    return contWindow


curses.wrapper(main)
