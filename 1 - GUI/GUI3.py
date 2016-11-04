from tkinter import *
import tkinter.ttk as ttk

class Tableview(Frame):

    def __init__(self,fenetre):
        Frame.__init__(self,fenetre)
        self.pack()
        self.tree = ttk.Treeview(self)
        self.tree["columns"]=("Nom","Taille","Poids","Age","Sexe")
        self.tree.column("Nom", width=50 )
        self.tree.column("Taille", width=50)
        self.tree.column("Poids", width=50)
        self.tree.column("Age", width=50)
        self.tree.column("Sexe", width=50)
        self.tree.heading("Nom", text="Nom")
        self.tree.heading("Taille", text="Taille")
        self.tree.heading("Poids", text="Poids")
        self.tree.heading("Age", text="Age")
        self.tree.heading("Sexe", text="Sexe")
        self.tree.pack()

    def insertion(self,objet):
        self.tree.insert('', 'end', 'test', text='test1',values=("1A","1b"))
        

fenetre=Tk()
app=Tableview(fenetre)
app.insertion(2)
app.mainloop()
app.destroy()
