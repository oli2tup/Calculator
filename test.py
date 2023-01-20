 #--------------------------------------------------------------#
# Making a donwloadable calulcator with GUI using Python 
# Basic project

# Making the GUI 
# programming the buttons 
# make it downloadable
 #--------------------------------------------------------------#
 #!usr/bin/python 
 
from tkinter import ttk 
from tkinter import *

window = Tk()
frm = ttk.Frame(window, padding = 10)
frm. grid()


# keeping all the buttons in on array in the format i want them to appear
buttons = [[7, 8, 9, "÷"],
           [4, 5, 6, "x"],
           [1, 2, 3, "-"],
           ["=", ".", 0, "+"]]

for row in range (0, 4):        # staring the button at row 4 ending row 7
    for column in range (0, 4): # starting the buttons at columns 0 to 3 
              
        ttk.Button(frm, text = str(buttons[row][column]), textvariable = buttons[row][column]).grid(column = column , row = row + 4)    
        
ttk.Button(frm, text = "Quit", command = window.destroy).grid(column = 3,row = 0)

window.mainloop()