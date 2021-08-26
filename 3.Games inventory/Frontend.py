"""
A program for games inventory with the information:
Title, Genre, Publisher, Release Date, Rating, Developer

Operations:
1. View all games
2. Search a game 
3. Update a game
4. Delete a game
5. Get rating
"""

from tkinter import *
from Backend import Database

window = Tk()
database = Database()

def get_selected_row(event):
    global selected_tuple
    try:
        index=list_of_games.curselection()[0]
        selected_tuple=list_of_games.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
        e5.delete(0,END)
        e5.insert(END,selected_tuple[5])
        e6.delete(0,END)
        e6.insert(END,selected_tuple[6])
    except IndexError:
        pass

def view_command():
    list_of_games.delete(0,END)
    for row in database.view():
        list_of_games.insert(END,row)

def search_command():
    list_of_games.delete(0,END)
    for row in database.search(e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get(),e5_value.get(),e6_value.get()):
        list_of_games.insert(END,row)

def add_command():
    database.insert(e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get(),e5_value.get(),e6_value.get())
    list_of_games.delete(0,END)
    list_of_games.insert(END,(e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get(),e5_value.get(),e6_value.get()))

def delete_command():
    database.delete(int(selected_tuple[0]))

def update_command():
    database.update(selected_tuple[0],e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get(),e5_value.get(),e6_value.get())

def show_rating_command():
    list_of_games.delete(0,END)
    for row in database.max_rating():
        list_of_games.insert(END,row)

def latest_command():
    list_of_games.delete(0,END)
    for row in database.latest_games():
        list_of_games.insert(END,row)

def best_inyear_command():
    list_of_games.delete(0,END)
    for row in database.best_in_year():
        list_of_games.insert(END,row)

def sorted_games_command():
    list_of_games.delete(0,END)
    for row in database.sorted_games():
        list_of_games.insert(END,row)

def games_by_genre_command():
    list_of_games.delete(0,END)
    for row in database.games_by_genre():
        list_of_games.insert(END,row)

def best_by_genre_command():
    list_of_games.delete(0,END)
    for row in database.best_by_genre():
        list_of_games.insert(END,row)


window.wm_title("Games inventory")

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
list_of_games = Listbox(window,height=6, width=40)
list_of_games.grid(row=2, column = 1, rowspan = 6, columnspan=3)

# create the scroll bar
sb1 = Scrollbar(window, orient=VERTICAL)
sb1.grid(row=2,column=4,rowspan=6, sticky=NS)
list_of_games.configure(yscrollcommand=sb1.set)
sb1.configure(command=list_of_games.yview)

list_of_games.bind('<<ListboxSelect>>',get_selected_row)

# create all buttons
b1 = Button(window,text="View all games",width=12,command=view_command)
b1.grid(row = 2,column = 5)
b1 = Button(window,text="Add new game",width=12,command=add_command)
b1.grid(row = 3,column = 5)
b2 = Button(window,text="Search a game",width=12,command=search_command)
b2.grid(row = 4,column = 5)
b3 = Button(window,text="Update a game",width=12,command=update_command)
b3.grid(row = 5,column = 5)
b4 = Button(window,text="Delete a game",width=12,command=delete_command)
b4.grid(row = 6,column = 5)
b5 = Button(window,text="Show best games",width=12,command=show_rating_command)
b5.grid(row = 7,column = 5)
b6=Button(window,text="Close", width=12,command=window.destroy)
b6.grid(row=8,column=5)

b7 = Button(window,text="Show latest games",width=12,command=latest_command)
b7.grid(row = 2,column = 6)
b8 = Button(window,text="Best games in 2021",width=12,command=best_inyear_command)
b8.grid(row = 3,column = 6)
b9 = Button(window,text="Show sorted games",width=12,command=sorted_games_command)
b9.grid(row = 4,column = 6)
b10 = Button(window,text="Games by genre",width=12,command=games_by_genre_command)
b10.grid(row = 5,column = 6)
b11 = Button(window,text="Best in genre",width=12,command=best_by_genre_command)
b11.grid(row = 6,column = 6)

window.mainloop()
