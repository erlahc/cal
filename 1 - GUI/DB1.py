import sqlite3

def addtobase(nom, taille, poids, age, sexe):
    conn =sqlite3.connect("db1.db") 
    cur =conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name TEXT,
     taille FLOAT,
     poids FLOAT,
     age INTEGER,
     sexe TEXT)""")
    cur.execute("""
    INSERT INTO users(name, taille, poids, age, sexe)
    VALUES(?, ?, ?, ?, ?)""", (nom,taille,poids,age,sexe))
    conn.commit()
    conn.close()

def getlist():
    conn =sqlite3.connect("db1.db") 
    cur =conn.cursor()
    cur.execute("""SELECT * FROM users LIMIT 5""")
    a=list(cur.fetchall())
    return a
