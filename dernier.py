import copy
import datetime
from operator import mod
customer = {
    'name' : "",
    'phone_number' : 0
}
item = {
    'name' : "",
    'qty' : 0,
    'price' : 0
}
commande = {
    'client' : "",
    'article' : "",
    'qty' : 0,
    'total' : 0,
    'date' : ""
}
point = {
    'client' : "",
    'points' : 0
}

catalogue = []
liste_clients = []
achats = []
pointage = []

#ajout d'un client
def ajout_client(name, phone):
    currentclient = copy.deepcopy(customer)
    currentclient['name'] = name
    currentclient['phone_number'] = phone
    liste_clients.append(currentclient)
    return currentclient

#ajout d'un article
def ajout_article(name, qty, price):
    current_item = copy.deepcopy(item)
    current_item['name'] = name
    current_item['qty'] = qty
    current_item['price'] = price
    print('larticle a bien été ajouté')
    catalogue.append(current_item)
    return current_item

def commandes():
    client = input('entrer le nom du client : ')
    for acheteur in liste_clients:
        if client.lower() == acheteur['name'].lower() :
            rep =input('voulez vous ajouter des produits dans votre panier ? (oui/non)')
            while rep == 'oui':
                produit = input('entrer le nom de larticle : ')
                for item in catalogue :
                    if produit.lower() == item['name'].lower() :
                        qte = input('quelle quantité en voulez vous ? ')
                        if item['qty'] >= int(qte) :
                            item['qty'] -= int(qte)
                            montant = item['price'] * int(qte)
                            print('vous devez payer {} '.format(montant))
                            current_achat = copy.deepcopy(commande)
                            current_achat['client'] = client
                            current_achat['article'] = produit
                            current_achat['qty'] = qte
                            current_achat['total'] = montant
                            current_achat['date'] = datetime.date.today()
                            achats.append(current_achat)
                        elif item['qty'] < int(qte) :
                            print('Quantité trop grande diminuez là : ')
                            return qte
                        else :
                            print('article indisponible')
                    else :
                        print('article indisponible')

def points():
    total = 0
    nbre_point = 0
    client = input('entrer le nom du client : ')
    for acheteur in achats :
        if client.lower() == acheteur['client'].lower() :
            total += acheteur['total']        
        print(total)
        nbre_point = (total / 10000)
        nbre_point = int(nbre_point)
        print('vous avez {} points'.format(nbre_point))
        current_point = copy.deepcopy(point)
        current_point['client'] = client
        current_point['points'] = nbre_point
        pointage.append(current_point)

def reglement():
    client = input('entrer le nom du client : ')
    for acheteur in 
    rep = input('comment voulez vous regler votre facture en especes ? ou par points cummulés? ')
    if rep == 'especes':
        print('facture réglée')
    else:

    
     

    
    


ajout_client('leo', 698542603)
ajout_client('mum', 694275126)
ajout_article('bonbon', 25, 25500)
ajout_article('miel', 50, 305550)
print(catalogue)
commandes()
print(achats)
points()
print(pointage)


            



#ajout_article("bonbon", 25, 1250)
#ajout_article("biscuit", 25, 1250)
#print(catalogue)
