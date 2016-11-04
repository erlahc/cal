from tkinter import *
import DB1
import GUI2

fenetre = Tk()

label_nom = Label(fenetre,text="Nom")
label_nom.pack()
var_text_nom = StringVar()
text_nom = Entry(fenetre,textvariable=var_text_nom, width =30)
text_nom.pack(anchor = W)

label_taille = Label(fenetre,text="Taille")
label_taille.pack()
var_text_taille = StringVar()
text_taille = Entry(fenetre,textvariable=var_text_taille, width =30)
text_taille.pack(anchor = W)

label_poids = Label(fenetre,text="Poids")
label_poids.pack()
var_text_poids = StringVar()
text_poids = Entry(fenetre,textvariable=var_text_poids, width =30)
text_poids.pack(anchor = W)

label_age = Label(fenetre,text="Age")
label_age.pack()
var_text_age = StringVar()
text_age = Entry(fenetre,textvariable=var_text_age, width =30)
text_age.pack(anchor = W)

var_choix_sexe = StringVar()
var_choix_sexe.set("homme")
choix_homme = Radiobutton(fenetre,text="Homme",variable=var_choix_sexe,value="homme")
choix_femme = Radiobutton(fenetre,text="Femme",variable=var_choix_sexe,value="femme")
choix_homme.pack(anchor = W)
choix_femme.pack(anchor = W)

bouton_valider = Button(fenetre,text="Valider", command = fenetre.quit)
bouton_valider.pack()

fenetre.mainloop()

"""tests"""
try:
    nom = var_text_nom.get()
    taille = float(var_text_taille.get())
    poids = float(var_text_poids.get())
    age = int(var_text_age.get())
    sexe = var_choix_sexe.get()
    DB1.addtobase(nom,taille,poids,age,sexe)
    fenetre.destroy()
    GUI2.displaylist()
except:
    print("Erreur dans les champs")


