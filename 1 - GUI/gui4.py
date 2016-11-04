from tkinter import *
import tkinter.ttk as ttk

class gui(Frame):

    def __init__(self,fenetre):
        Frame.__init__(self,fenetre)
        self.grid(row=0,column=0)
        
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

        Button(self,text='Ajouter',command=self.quit).grid(row=4, column=0,sticky=W)

        tree=ttk.Treeview(self,columns=['Host', 'Event', 'Date', 'Time', 'Text'], show='headings')
        tree.grid(row=5, column=0, columnspan=2)
        
fenetre=Tk()
app=gui(fenetre)
app.mainloop()
app.destroy()
