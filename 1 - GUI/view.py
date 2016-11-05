from tkinter import *
import tkinter.ttk as ttk
import model
import controler

class gui(Tk):

    def __init__(self):
        Tk.__init__(self)
        
        Label(self,text="Nom").grid(row=0, column=0, sticky=W)
        nom=StringVar()
        Entry(self,textvariable=nom,width=15).grid(row=0, column=1)
        
        Label(self,text="Taille").grid(row=1, column=0, sticky=W)
        taille=StringVar()
        Entry(self,textvariable=taille,width=15).grid(row=1, column=1)
                                                   
        Label(self,text="Poids").grid(row=2, column=0, sticky=W)
        poids=StringVar()
        Entry(self,textvariable=poids,width=15).grid(row=2, column=1)
                                                   
        Label(self,text="Age").grid(row=3, column=0, sticky=W)
        age=StringVar()
        Entry(self,textvariable=age,width=15).grid(row=3, column=1)

        Button(self,text='Ajouter',command=self.quit).grid(row=4, column=0, sticky=W)

        self.tree=ttk.Treeview(self,columns=['Nom', 'Taille', 'Poids', 'Age', 'Sexe'], show='headings')
        self.tree.column('Nom', width = 70)
        self.tree.heading('Nom', text='Nom')
        self.tree.column('Taille', width = 30)
        self.tree.heading('Taille', text='Taille')
        self.tree.column('Poids', width = 30)
        self.tree.heading('Poids', text='Poids')
        self.tree.column('Age', width = 30)
        self.tree.heading('Age', text='Age')
        self.tree.column('Sexe', width = 50)
        self.tree.heading('Sexe', text='Sexe')
        self.tree.bind("<Double-1>", self.OnDoubleClick)
        self.tree.grid(row=5, column=0, columnspan=2)
        list_db=model.getlist()
        controler.filltreeview(self.tree,list_db)


    def OnDoubleClick(self,event):
        controler.deleteitem(self.tree)