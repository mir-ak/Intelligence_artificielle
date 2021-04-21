
import copy as copy
from math import sqrt
from collections import Counter
#On extrait toutes les données disponible sous forme de liste de fleur 
data_learn = []
for fleur in open("iris_learn_data"):
	fleur = fleur[:-2]
	fleur = fleur.split(";")
	temp = []
	for attribut in fleur:
		temp.append(float(attribut))
	data_learn.append(temp)

data_learn_label = []
for line in open("iris_learn_label"):
	line = int(line[:-2])
	data_learn_label.append(line)
data_test = []
for fleur in open("iris_test_data"):
	fleur = fleur[:-2]
	fleur = fleur.split(";")
	temp = []
	for attribut in fleur:
		temp.append(float(attribut))
	data_test.append(temp)

data_test_label = []
for line in open("iris_test_label"):
	line = int(line[:-2])
	data_test_label.append(line)

def distance_fleur(fleurX,fleurY):
#Retourne la distance entre 2 fleurs
	resultat = 0
	for attributY, attributX in zip(fleurX,fleurY):
		resultat += pow(attributX - attributY, 2)
	resultat = sqrt(resultat)
	return resultat

def genese_comparatif(fleur_a_comparer):
	resultat = []
	for i in range(len(data_learn)):
		resultat.append((distance_fleur(data_learn[i],fleur_a_comparer),data_learn_label[i]))	
	resultat = sorted(resultat, key = lambda x:x[0])
	return resultat

def traitement_voisins(liste_voisins):
	resultat = dict()
	for elem in liste_voisins:
		if elem[1] not in resultat:
			resultat.update({elem[1]:[elem[0],1]})
		else:
			resultat.update({elem[1]: [resultat[elem[1]][0] +elem[0], resultat[elem[1]][1] +1]})
		return resultat
def K_ppv(fleur,k):
	liste_voisins = genese_comparatif(fleur)
	liste_voisins_K = []
	i = 0
	while(i < k):
		liste_voisins_K.append(liste_voisins[i])
		i += 1

	derniere_distance = liste_voisins_K[-1][0]
	while(i < len(data_learn) and liste_voisins[i][0] == derniere_distance): 
		liste_voisins_K.append(liste_voisins[i])
		i += 1
	liste_voisins_K_traite = traitement_voisins(liste_voisins_K)
	maxi = None
	for classe in liste_voisins_K_traite:
		if(maxi is None):
		#Si max n'est pas definie
			maxi = [classe,liste_voisins_K_traite[classe][1],liste_voisins_K_traite[classe][0]]
		elif(maxi[1] < liste_voisins_K_traite[classe][1]):
		#Si trouve une classe qui a plus d'occurence  	
			maxi = [classe,liste_voisins_K_traite[classe][1],liste_voisins_K_traite[classe][0]]
		elif(maxi[1] == liste_voisins_K_traite[classe][1]):
		#Si trouve une classe qui a autant d'occurence  	
			if maxi[2] > liste_voisins_K_traite[classe][0]:
			#si cette classe est globalement plus proche alors il devient maxi
				maxi = [classe,liste_voisins_K_traite[classe][1],liste_voisins_K_traite[classe][0]]

	print(maxi)

	return maxi[0] 

def sol():
	
	statistique = []
	for k in range(2,11):
		print("Prediction par K-ppv : classe réelle Pour K =",k)
		liste_prediction = []
		for fleur in data_test:
			liste_prediction.append(K_ppv(fleur,k))
		nb_reussite = 0 
		for i in range(len(liste_prediction)):
			if liste_prediction[i] == data_test_label[i]:
				print("\t",liste_prediction[i]," : ",data_test_label[i],"Reussite")
				nb_reussite +=1
			else:
				print("\t",liste_prediction[i]," : ",data_test_label[i],"Echec")
		taux_reussite = nb_reussite / len(liste_prediction)
		statistique.append([k,taux_reussite])
	print(statistique)
sol()

