import sqlite3

class Database:

    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cur = self.connection.cursor() #open connection

        self.cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.connection.commit()

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO books VALUES (NULL, ?,?,?,?)", (title, author, year, isbn))
        self.connection.commit()  #commit changes to db

    def view(self):
        self.cur.execute("SELECT * FROM books")
        rows = self.cur.fetchall()
        return rows

    def search(self, title="", author="", year="", isbn=""):  ##empty strings are to prevent required parameter fields if user doesn't pass any
        self.cur.execute("SELECT * FROM books WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM books WHERE id = ?", (id,))
        self.connection.commit()  #commit changes to db

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE books SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
        self.connection.commit()  #commit changes to db

    def __del__(self):
        self.connection.close()



# update(3, "Goodwill Hunting", "Tim Sykes", 1854, 29294)
# update(4, "Harry Potter and the Half Blood Prince", "J.K. Rowling", 2005, 999999)
# print(view())
