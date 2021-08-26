"""
A program for games inventory with the information:
Title, Genre, Publisher, Developer, Release Date, Rating

Operations:
1. View all games
2. Search a game 
3. Update a game
4. Delete a game
5. Get rating
"""

from tkinter import *

window = Tk()

# create first row
l1 = Label(window,text="Title")
l1.grid(row = 0,column = 0)
e1_value = StringVar()
e1 = Entry(window,textvariable = e1_value)
e1.grid(row = 0, column = 1)
l2 = Label(window,text="Genre")
l2.grid(row = 0,column = 2)
e2_value = StringVar()
e2 = Entry(window,textvariable = e2_value)
e2.grid(row = 0, column = 3)
l3 = Label(window,text="Publisher")
l3.grid(row = 0,column = 4)
e3_value = StringVar()
e3 = Entry(window,textvariable = e3_value)
e3.grid(row = 0, column = 5)

# create second row
l4 = Label(window,text="Developer")
l4.grid(row = 1,column = 0)
e4_value = StringVar()
e4 = Entry(window,textvariable = e4_value)
e4.grid(row = 1, column = 1)
l5 = Label(window,text="Release Date")
l5.grid(row = 1,column = 2)
e5_value = StringVar()
e5 = Entry(window,textvariable = e5_value)
e5.grid(row = 1, column = 3)
l6 = Label(window,text="Rating")
l6.grid(row = 1,column = 4)
e6_value = StringVar()
e6 = Entry(window,textvariable = e6_value)
e6.grid(row = 1, column = 5)

# create the box
list_of_games = Listbox(window,height=6, width=30)
list_of_games.grid(row=2, column = 0, rowspan = 6, columnspan=3)

# create the scroll bar
sb1 = Scrollbar(window)
sb1.grid(row=2,column=3,rowspan=6)
list_of_games.configure(yscrollcommand=sb1.set)
sb1.configure(command=list_of_games.yview)

# create all buttons
b1 = Button(window,text="View all games")
b1.grid(row = 2,column = 5)
b2 = Button(window,text="Search a games")
b2.grid(row = 3,column = 5)
b3 = Button(window,text="Update a games")
b3.grid(row = 4,column = 5)
b4 = Button(window,text="Delete a games")
b4.grid(row = 5,column = 5)
b5 = Button(window,text="Show rating")
b5.grid(row = 6,column = 5)

window.mainloop()
