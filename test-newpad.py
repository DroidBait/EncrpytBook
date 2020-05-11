import os
import curses
import curses.textpad

def main(stdscr):
    h, w = stdscr.getmaxyx()
    curses.curs_set(0)
    currentRow = 0
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    listLength = 0
    currentRow = 0
    menu = ["11", "22", "33", "44", "55", "66", "88", "99", "101"]
    listLength = len(menu)
    if listLength > 8:
        listLength = 8
    startList = 0
    endList = 8
    entryMode = 'exit'

    while 1:

        #if currentRow == endList:
        #    startList += 1
        #    endList += 1

        key = stdscr.getch()

        if key == curses.KEY_UP and currentRow > 0:
            currentRow -= 1
            if currentRow == startList and startList > 0:
                startList -= 1
                endList -= 1
        elif key == curses.KEY_DOWN and currentRow < listLength - 0:
            currentRow += 1
            if currentRow == listLength - 1 and endList <= len(menu):
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
            entryMode = 'start'

        

        printScreen(h, w, currentRow, menu, listLength, startList, endList, entryMode)


def printScreen(height, width, currentRow, menu, listLength, startList, endList, entryMode):
    #test
    #win = curses.newpad(10, 15)
    win = curses.newwin(10, 5, 0, 0)
    win.border(1)
    #win.addstr(1, 1, "test")
    #menu = ["11", "22", "33", "44", "55", "66", "88", "99"]
    loopNum = 0

    #########################
    ## Working scroll code ##
    #########################
    for idx, row in enumerate(menu):
        if idx >= startList and idx < endList:
            if idx == currentRow:
                win.attron(curses.color_pair(1))
                win.addstr(loopNum + 1, 0, str(startList) + " " + str(endList))
                win.attroff(curses.color_pair(1))
            else:
                win.addstr(loopNum + 1, 0, row)
            loopNum += 1

    #win.refresh(0, 0, 0, 0, 20, 20)

    win2 = window2(entryMode)
    win2.refresh()
    win.refresh()


def window2(entryMode):
    sss = curses.newwin(10, 30, 0, 10)
    sss.border(1)
    step = "step1"
    curses.flushinp()
    while entryMode != 'exit':
        if entryMode == 'exit':
            sss.addstr(1, 1, "Type a to start\n")
        else:
            if step == "step1":
                curses.echo()
                sss.addstr(1, 1, "step 1")
                var1 = sss.getstr(2, 1, 10)
                #sss.refresh()
                sss.addstr(3, 1, var1)
                #tb = curses.textpad.Textbox(sss, insert_mode=True)
                #text = tb.edit()
                #sss.addstr(4,1, text)
                curses.noecho()
                curses.cbreak()
                step = "step2"
                entryMode = 'exit'
        #sss.addstr(1, 1, "start entry")

    return sss



curses.wrapper(main)