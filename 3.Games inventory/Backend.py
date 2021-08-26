import sqlite3

class Database:

    def __init__(self):
        self.conn=sqlite3.connect("3.Games inventory/games.db")
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS games (id INTEGER PRIMARY KEY, title text, genre text, publisher text,developer text, releaseDate date, rating integer)")
        self.conn.commit()

    def insert(self,title,genre,publisher,developer,relese_date, rating):
        self.cur.execute("INSERT INTO games VALUES (NULL,?,?,?,?,?,?)",(title,genre,publisher,developer,relese_date, rating))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM games")
        rows=self.cur.fetchall()
        return rows

    def search(self,title="",genre = "",publisher = "" ,developer = "", relese_date = "", rating = ""):
        self.cur.execute("SELECT * FROM games WHERE title=? OR genre=? OR publisher=? OR developer =? OR releaseDate=? OR rating=?", (title,genre,publisher,developer,relese_date,rating))
        rows=self.cur.fetchall()
        return rows

    def max_rating(self):
        self.cur.execute("SELECT title,rating FROM games WHERE rating = (SELECT MAX(rating) FROM games); ")
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM games WHERE id=?",(id,))
        self.conn.commit()

    def update(self,id,title,genre,publisher,developer,relese_date, rating):
        self.cur.execute("UPDATE games SET title=?, genre=?, publisher=?,developer=?, releaseDate=?, rating=? WHERE id=?",(title,genre,publisher,developer,relese_date,rating,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
    
    def deleteTable(self):
        self.cur.execute("DROP TABLE games;")
        self.conn.commit()


