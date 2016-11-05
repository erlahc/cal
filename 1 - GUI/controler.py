import model

def filltreeview(treeobj,list_db):
    for i in list_db:
        treeobj.insert("",'end',text=str(i.iddb), values=(i.nom,i.taille,i.poids,i.age,i.sexe))


##move to gui
def deleteitem(treeobj):
    item = treeobj.selection()[0]
    item_id = treeobj.item(item,'text')
    treeobj.delete(item)
    model.deletelist(item_id)

##move to gui
def additem(treeobj,i):
    treeobj.insert("",'end',text=str(i.iddb), values=(i.nom,i.taille,i.poids,i.age,i.sexe))
    model.insertlist(i)
