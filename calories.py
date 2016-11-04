import math

class People:

	def __init__(self, nom ='charles', taille = 1.80, poids = 72, age = 25, sexe = 'male'):
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


people1 = People()
print(metabolismebase(people1))



