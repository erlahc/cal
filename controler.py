import model

def filltreeview(treeobj,list_db):
    for i in list_db:
        treeobj.insert("",'end',text=str(i.iddb), values=(i.nom,i.taille,i.poids,i.age,i.sexe,i.metabolismebase()))
##move to gui
def deleteitem(treeobj):
    item = treeobj.selection()[0]
    item_id = treeobj.item(item,'text')
    treeobj.delete(item)
    model.deletelist(str(item_id))

##move to gui
def additem(treeobj,i):
    try:
        i.iddb=int(i.iddb)
        i.nom=str(i.nom)
        i.taille=float(i.taille)
        i.poids=float(i.poids)
        i.age=int(i.age)
        i.sexe=str(i.sexe)
        treeobj.insert("",'end',text=str(i.iddb), values=(i.nom,i.taille,i.poids,i.age,i.sexe,i.metabolismebase()))
        model.insertlist(i)
    except:
        print('input error')

def edititem(treeobj,i):
    try :
        i.iddb=int(i.iddb)
        i.nom=str(i.nom)
        i.taille=float(i.taille)
        i.poids=float(i.poids)
        i.age=int(i.age)
        i.sexe=str(i.sexe)
        item = treeobj.selection()[0]
        item_id = treeobj.item(item,'text')
        i.iddb=int(item_id)
        treeobj.item(item,values=(i.nom,i.taille,i.poids,i.age,i.sexe,i.metabolismebase()))
        model.editlist(i)
    except :
        print('input error')
