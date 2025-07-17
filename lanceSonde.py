
import time
import requests

import datetime
import json

import matplotlib.pyplot as plt

# Suppression des Warning URLLIB3
import urllib3
urllib3.disable_warnings()


fichierDATA = "sondeSite.json"

def pingsite(hostanalyse):
    debut = time.time()
    #r = requests.get(hostanalyse, proxies=proxies, verify='FiddlerRoot.pem')
    r = requests.get(hostanalyse,verify=False)
    fin = time.time()
    duree = round((fin - debut)*1000) 
    print("Temps de réponse du site : " + hostanalyse + " - " + str(duree) + "ms")
    return duree, r.status_code

# Récuépration des valeurs depuis un fichier de données
print("Lecture des données depuis le fichier : " + fichierDATA)
with open(fichierDATA, 'r') as file :   
   data = json.load(file) 
file.close()

host="https://myriamdupouy.com"

Now = datetime.datetime.now()
DateSonde = Now.strftime('%d/%m/%Y')
TimestanpSonde = Now.strftime('%I:%M%p')

# Lancement de la requette pour connaitre le temps de réponse et status de la transaction
dureetransaction, statuscode = pingsite(host)

# Ajout d'un element dans la liste
data.append({"host":host,"Tdr":dureetransaction,"Status":statuscode,"date":DateSonde,"heure":TimestanpSonde})

# Transformation de la chaine de caractère en format list (json)
dataJson = json.dumps(data)

# Ecriture dans le fichier de données avec la nouvelle occurence
with open(fichierDATA, 'w') as fileWrite :   
   fileWrite.write(str(dataJson))
fileWrite.close()

# Affichage des données uniquement pour la clé "Tdr" (Temps de Réponse)
#for cle in data:
#    print(cle['Tdr'])


# Gestion du graphique

labels = ['03:14', '043:14', '05:14', '06:14', '07:14']
Tdr = [230,540,1230,580,344]

#plt.plot(labels,Tdr, marker='o', linestyle='dashed')

#plt.ylabel('Temps de réponse (ms)')
#plt.xlabel('Heure')
#
#ax = plt.gca()
#
## recompute the ax.dataLim
#ax.relim()
## update ax.viewLim using the new dataLim
#ax.autoscale_view()
##plt.draw()
#
#plt.show()
#