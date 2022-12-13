from tkinter import *
from tkinter import ttk
import pyautogui as pg
import time
from datetime import datetime
from pytz import timezone


def carrier_specific_fill():
    pg.doubleClick(1693, 348)
    pg.press('y')
    pg.press('tab')
    pg.press('tab')

    pg.press('n')
    pg.press('tab')

    pg.typewrite('ot')
    pg.press('tab')

    pg.press('n')
    pg.press('tab')

    pg.press('n')
    pg.press('tab')

    pg.press('n')
    pg.press('tab')
    pg.press('tab')

    pg.press('n')
    pg.press('tab')

    pg.press('y')
    pg.press('tab')

    pg.press('n')
    pg.press('tab')

    pg.press('n')
    pg.press('tab')

    pg.press('y')
    pg.press('tab')

    pg.press('y')
    pg.press('tab')

    pg.press('y')
    pg.press('tab')

    pg.click(1813, 191)


def quote_results_fill():
    pg.click(1072, 535)
    pg.click(1278, 715)

    pg.click(1301, 660)

    pg.click(1301, 660)


def apol_auto_fill():
    # Click Tasks
    pg.click(370, 405)

    # Click put Attachments - send app
    pg.click(796, 494)
    pg.keyDown('shift')
    pg.click(808, 546)
    pg.keyUp('shift')
    time.sleep(2)

    # Click edit
    pg.click(280, 504)

    time.sleep(1)

    # Click status and change to complete
    pg.click(687, 364)
    pg.click(891, 358)
    pg.hotkey('ctrl', 'a', 'c')
    pg.typewrite('Completed')
    pg.click(1079, 733)

    time.sleep(2)

    pg.click(818, 628)
    pg.keyDown('ctrl')
    pg.press('down')
    time.sleep(1)
    pg.click(818, 628)
    pg.press('down')
    time.sleep(1)
    pg.click(818, 628)
    pg.press('down')
    time.sleep(1)
    pg.press('down')
    time.sleep(1)
    pg.click(818, 628)
    pg.keyUp('ctrl')
    time.sleep(3)

    # Click edit
    pg.click(280, 504)

    # Click status and change to complete
    pg.click(687, 364)
    time.sleep(2)
    pg.click(891, 358)
    pg.hotkey('ctrl', 'a', 'c')
    pg.typewrite('Not Applicable')
    pg.click(1079, 733)

    time.sleep(3)

    pg.click(822, 600)

    # Click edit and change owner
    pg.click(280, 504)
    time.sleep(2)
    pg.doubleClick(781, 246)
    pg.typewrite('POLKYE')
    pg.press('tab')
    pg.click(1175, 807)

    time.sleep(2)

    # Change who/owner
    pg.doubleClick(721, 250)
    pg.typewrite('POLRA1')
    pg.press('tab')


def apol_home_fill():
    # Click Tasks
    pg.click(370, 405)

    # Click put Attachments - send app
    pg.click(796, 494)
    pg.keyDown('shift')
    pg.click(808, 546)
    pg.keyUp('shift')
    time.sleep(2)

    # Click edit
    pg.click(280, 504)

    time.sleep(2)

    # Click status and change to complete
    pg.click(687, 364)
    pg.click(891, 358)
    pg.hotkey('ctrl', 'a', 'c')
    pg.typewrite('Completed')
    pg.click(1079, 733)

    time.sleep(2)

    # Select Send EOI, change Owner, and edit Start date
    pg.click(818, 628)  # Send EOI
    pg.click(280, 504)  # Edit
    time.sleep(2)
    pg.doubleClick(758, 369)  # Start
    pg.typewrite(datetime.now(timezone('America/Chicago')).strftime('%m/%d/%Y'))    # Type central date
    pg.press('tab')
    pg.click(1175, 807)  # Finish
    time.sleep(2)

    # Select Did this close
    pg.press('down')
    time.sleep(2)
    pg.click(280, 504)  # Edit
    time.sleep(2)
    pg.click(826, 339)  # Status
    pg.hotkey('ctrl', 'a', 'c')
    pg.typewrite('Not Applicable')
    time.sleep(1)
    pg.press('tab')
    pg.click(1175, 807)  # Finish

    # Select FU PMT and change owner
    pg.press('down')
    time.sleep(2)
    pg.press('down')
    pg.click(280, 504)  # Edit
    time.sleep(2)
    pg.doubleClick(793, 249)    # Owner
    pg.typewrite('POLKYE')
    time.sleep(1)
    pg.press('tab')
    pg.click(1175, 807)  # Finish

    # Select EOI/HOI and change Owner and status
    time.sleep(2)
    pg.press('down')
    pg.click(280, 504)  # Edit
    time.sleep(2)
    pg.doubleClick(793, 249)  # Owner
    pg.typewrite('POLKYE')
    time.sleep(2)
    pg.press('tab')
    pg.typewrite('Completed')
    pg.press('tab')
    time.sleep(1)
    pg.click(1175, 807)  # Finish

    # Change who/owner
    time.sleep(2)
    pg.doubleClick(721, 250)
    pg.typewrite('POLRA1')
    pg.press('tab')


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Carrier Specific Fill", command=carrier_specific_fill).grid(column=2, row=0)
ttk.Button(frm, text="APOL auto fill", command=apol_auto_fill).grid(column=3, row=0)
ttk.Button(frm, text="APOL home fill", command=apol_home_fill).grid(column=4, row=0)
# ttk.Button(frm, text="Quote Results Fill", command=quote_results_fill).grid(column=3, row=0)
root.mainloop()
