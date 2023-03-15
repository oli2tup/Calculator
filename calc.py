 #---------------------------------------------------------------------------------------#
# Making a donwloadable calulcator with GUI using Python 
# Basic project
# programming the buttons 
# Making the GUI 
# make it downloadable

#!usr/bin/python 
 
from tkinter import ttk 
from tkinter import *

window = Tk()
window.title("Calculator")
window.maxsize(600, 300)

top_frame = ttk.Frame(window, padding = 10)
top_frame.grid(row = 0, column = 0)

frm = ttk.Frame(window, padding = 5)
frm. grid(row = 1, column = 0)

# Text Field

field = Text(top_frame, height = 2, width = 30)
field.grid(column = 0, row = 0)

#---------------------------------------------------------------------------------------#
# button functionality 
def clicked(num):
    '''action for when the button is clicked'''

    field.insert(INSERT, 0)

#---------------------------------------------------------------------------------------#
# keeping all the buttons in on array in the format i want them to appear
buttons = [["Quit", "( )", "%", "÷"],
           [7, 8, 9, "x"],
           [4, 5, 6, "-"],
           [1, 2, 3, "+"],
           [0, ".", "⌫", "="]]


for row in range (0, 5):        # staring the button at row 4 ending row 7
    for column in range (0, 4): # starting the buttons at columns 0 to 3 

        button_text = buttons[row][column]
        button = ttk.Button(frm, text = button_text, 
                            command = clicked(button_text), textvariable= button_text)
        button.grid(column = column , row = row + 4)
        #print(button_text)

#---------------------------------------------------------------------------------------#


window.mainloop()