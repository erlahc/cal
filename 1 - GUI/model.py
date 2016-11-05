import sqlite3
import math

class People:

    def __init__(self, iddb = 0, nom ='charles', taille = 1.80, poids = 72, age = 25, sexe = 'male'):
        self.iddb = iddb
        self.nom = nom
        self.taille = taille
        self.poids = poids
        self.age = age
        self.sexe = sexe

    def metabolismebase(person):
        if person.sexe == 'male':
            param = 259
        elif person.sexe == 'female':
            param = 230
        return round(param*math.pow(person.poids,0.48)*math.pow(person.taille,0.5)*math.pow(person.age,-0.13),0)

def droptable():
    conn =sqlite3.connect("db1.db") 
    cur =conn.cursor()
    cur.execute("""DROP TABLE IF EXISTS users""")
    conn.commit()
    conn.close()

def addtobase(objet):
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
    VALUES(?, ?, ?, ?, ?)""", (objet.nom,objet.taille,objet.poids,objet.age,objet.sexe))
    conn.commit()
    conn.close()

def getlist():
    conn =sqlite3.connect("db1.db") 
    cur =conn.cursor()
    cur.execute("""SELECT * FROM users""")
    a=list(cur.fetchall())
    list_db=list()
    for i in range(len(a)):
        people=People(a[i][0],a[i][1],a[i][2],a[i][3],a[i][4],a[i][5])
        list_db.append(people)
    return list_db

def insertlist(objet):
    conn =sqlite3.connect("db1.db") 
    cur =conn.cursor()
    cur.execute("""INSERT INTO users(name,taille,poids,age,sexe) VALUES (?,?,?,?,?)""",(objet.nom, objet.taille, objet.poids, objet.age, objet.sexe))
    conn.commit
    conn.close()

def deletelist(iddb):
    conn =sqlite3.connect("db1.db") 
    cur =conn.cursor()
    cur.execute("""DELETE FROM users WHERE id=?""",iddb)
    conn.commit
    conn.close()

