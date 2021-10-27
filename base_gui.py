from tkinter import *
from db1 import Database

database = Database("books.db")

class Interface(object):

    def __init__(self, window):
        self.window = window
        self.window.title("Book Inventory App")

        # Labels
        title_label = Label(window, text="Title")
        author_label = Label(window, text="Author")
        year_label  = Label(window, text="Year")
        isbn_label = Label(window, text="ISBN")

        # Entry Fields
        self.title_entry = StringVar()
        self.title = Entry(window, bd = 3, width = 20, textvariable = self.title_entry)

        self.author_entry = StringVar()
        self.author = Entry(window, bd = 3, width = 20, textvariable = self.author_entry)

        self.year_entry = StringVar()
        self.year = Entry(window, bd = 3, width = 20, textvariable = self.year_entry)

        self.isbn_entry = StringVar()
        self.isbn = Entry(window, bd = 3, width = 20, textvariable = self.isbn_entry)

        # Listbox
        self.list_box = Listbox(window, width=45)
        self.list_box.bind('<<ListboxSelect>>', self.get_selected_row)

        # Scrollbar
        scroll = Scrollbar(window)

        # Buttons
        view_all = Button(window, text= "View All", width = 12, command = self.view_command)
        search_entry = Button(window, text= "Search Entry", width = 12, command = self.search_command)
        add_entry = Button(window, text= "Add Entry", width = 12, command = self.add_command)
        update = Button(window, text= "Update", width = 12, command = self.update_command)
        delete = Button(window, text= "Delete", width = 12, command = self.delete_command)
        close = Button(window, text= "Close", width = 12, command = self.window.destroy)

        # Gridding Labels
        title_label.grid(row = 0, column = 0)
        author_label.grid(row = 0, column = 2)
        year_label.grid(row = 1, column = 0)
        isbn_label.grid(row = 1, column = 2)

        # Gridding Entry Fields
        self.title.grid(row = 0, column = 1)
        self.author.grid(row = 0, column = 3)
        self.year.grid(row = 1, column = 1)
        self.isbn.grid(row = 1, column = 3)

        # Gridding Listbox + Scroll
        self.list_box.grid(row = 2, column = 0, columnspan = 2, rowspan = 6)
        scroll.grid(row = 2, column = 2, rowspan = 6)
        self.list_box.configure(yscrollcommand = scroll.set)
        scroll.configure(command = self.list_box.yview)

        # Gridding Buttons
        view_all.grid(row = 2, column = 3)
        search_entry.grid(row = 3, column = 3)
        add_entry.grid(row = 4, column = 3)
        update.grid(row = 5, column = 3)
        delete.grid(row = 6, column = 3)
        close.grid(row = 7, column = 3)


    # functions for buttons
    def view_command(self):
        self.clearText()
        for row in database.view():
            self.list_box.insert(END, row)

    def search_command(self):
        self.clearText()
        for row in database.search(self.title_entry.get(), self.author_entry.get(), self.year_entry.get(), self.isbn_entry.get()):
            self.list_box.insert(END, row)

    def add_command(self):
        self.clearText()
        database.insert(self.title_entry.get(), self.author_entry.get(), self.year_entry.get(), self.isbn_entry.get())
        self.list_box.insert(END, "Record added.")

    # for when item is selected in list_box, event param is default to bind function
    def get_selected_row(self, event):
        global selected_tuple  # global variable to reference outside of function
        if len(self.list_box.curselection()) > 0:  #if there are any items in listbox - can also use 'try' 'catch indexerror'
            index = self.list_box.curselection()[0]  # getting index for the record that was selected
            selected_tuple = self.list_box.get(index)  # storing the record using the index the cursor selected

            #writing selected record into new entry fields
            self.title.delete(0, END)
            self.title.insert(END, selected_tuple[1])
            self.author.delete(0, END)
            self.author.insert(END, selected_tuple[2])
            self.year.delete(0, END)
            self.year.insert(END, selected_tuple[3])
            self.isbn.delete(0, END)
            self.isbn.insert(END, selected_tuple[4])

        else:
            print("No record is selected.")

    def delete_command(self):
        database.delete(selected_tuple[0])
        self.clearText()
        for row in database.view():
            self.list_box.insert(END, row)

    def update_command(self):
        database.update(selected_tuple[0], self.title_entry.get(), self.author_entry.get(), self.year_entry.get(), self.isbn_entry.get())
        self.clearText()
        for row in database.view():
            self.list_box.insert(END, row)

    # function to clear input
    def clearText(self):
        self.list_box.delete(0, "end")

#creating an empty window



#needed to close the program - always at end of code
window = Tk()
Interface(window)
window.mainloop()
