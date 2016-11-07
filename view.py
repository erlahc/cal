from tkinter import *
import tkinter.ttk as ttk
import model
import controler

class gui(Tk):

    def __init__(self):
        Tk.__init__(self)
        
        Label(self,text="Nom").grid(row=0, column=0, sticky=W)
        self.nom=StringVar()
        Entry(self,textvariable=self.nom,width=15).grid(row=0, column=1)
        
        Label(self,text="Taille").grid(row=1, column=0, sticky=W)
        self.taille=StringVar()
        Entry(self,textvariable=self.taille,width=15).grid(row=1, column=1)
                                                   
        Label(self,text="Poids").grid(row=2, column=0, sticky=W)
        self.poids=StringVar()
        Entry(self,textvariable=self.poids,width=15).grid(row=2, column=1)
                                                   
        Label(self,text="Age").grid(row=3, column=0, sticky=W)
        self.age=StringVar()
        Entry(self,textvariable=self.age,width=15).grid(row=3, column=1)

        self.sexe = StringVar()
        self.sexe.set('femme')
        bouton1 = Radiobutton(self, text='femme', variable=self.sexe, value='femme').grid(row=4, column=0)
        bouton2 = Radiobutton(self, text='homme', variable=self.sexe, value='homme') .grid(row=4, column=1)

        Button(self,text='Ajouter',command=self.OnValidationButton).grid(row=5, column=0, sticky=W)
        Button(self,text='Edit',command=self.OnEditButton).grid(row=5, column=3, sticky=E)
        Button(self,text='Supprimer',command=self.OnDeleteButton).grid(row=5, column=1, sticky=E)
        
        self.tree=ttk.Treeview(self,columns=['Nom', 'Taille', 'Poids', 'Age', 'Sexe','MB'], show='headings')
        self.tree.column('Nom', width = 70)
        self.tree.heading('Nom', text='Nom')
        self.tree.column('Taille', width = 40)
        self.tree.heading('Taille', text='Taille')
        self.tree.column('Poids', width = 40)
        self.tree.heading('Poids', text='Poids')
        self.tree.column('Age', width = 30)
        self.tree.heading('Age', text='Age')
        self.tree.column('Sexe', width = 50)
        self.tree.heading('Sexe', text='Sexe')
        self.tree.column('MB', width = 50)
        self.tree.heading('MB', text='MB')
        self.tree.grid(row=6, column=0, columnspan=2)
        list_db=model.getlist()
        controler.filltreeview(self.tree,list_db)

    def OnDeleteButton(self):
        controler.deleteitem(self.tree)

    def OnValidationButton(self):
        objet = model.People(0,self.nom.get(),self.taille.get(),self.poids.get(),self.age.get(),self.sexe.get())
        controler.additem(self.tree,objet)

    def OnEditButton(self):
        objet = model.People(0,self.nom.get(),self.taille.get(),self.poids.get(),self.age.get(),self.sexe.get())
        controler.edititem(self.tree,objet)
