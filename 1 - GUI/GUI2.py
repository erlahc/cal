from tkinter import *
import DB1

def click(event):
    print(str(event.widget.name))
    

def displaylist():
    liste_elements = DB1.getlist()
    fenetre = Tk()
    for i in range(0,5):
        for j in range(0,6):
            a = StringVar()
            a.set(str(liste_elements[i][j]))
            b=liste_elements[i][0]
            entree = Entry(fenetre,textvariable = a, width = 10)
            entree.bind("<Button-1>",click)
            entree.grid(row=i, column=j)
    fenetre.mainloop()

displaylist()
