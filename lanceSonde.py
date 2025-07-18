
import time
import requests

import datetime
import json

from pathlib import Path
from scipy.interpolate import interp1d

import matplotlib.pyplot as plt
import numpy as np

# Suppression des Warning URLLIB3
import urllib3
urllib3.disable_warnings()

WORKING_IN_GP = True

http_proxy  = "http://127.0.0.1:3128"
https_proxy = "http://127.0.0.1:3128"
ftp_proxy   = "ftp://127.0.0.1:3128"

proxies = { 
              "http"  : http_proxy, 
              "https" : https_proxy, 
              "ftp"   : ftp_proxy
            }

SufixeDATA = "sondeSite.json"
SufixeGRAPH = "graph"

if WORKING_IN_GP:
    host="https://testkube-enterprise-ui.dev.etat-ge.ch/"
    PrefixeDATA = "testkub_dev_"
    fichierDATA = PrefixeDATA + SufixeDATA
else:
    host="https://myriamdupouy.com"
    PrefixeDATA = "myriamdupouycom_"
    fichierDATA = PrefixeDATA + SufixeDATA
    
labels = json.loads("[]")
Tdr = json.loads("[]")

def pingsite(hostanalyse):
    debut = time.time()
    if WORKING_IN_GP:
        r = requests.get(hostanalyse, proxies=proxies, verify='FiddlerRoot.pem')
    else: 
        r = requests.get(hostanalyse,verify=False)
    fin = time.time()
    duree = round((fin - debut)*1000) 
    #print("Temps de réponse du site : " + hostanalyse + " - " + str(duree) + "ms")
    return duree, r.status_code

# Controle si le fichier source existe, sinon il est créé avec un [] (format json)
my_file = Path(fichierDATA)
if not my_file.is_file():
    print("Le fichier existe PAS")
    with open(fichierDATA, 'w') as fileWrite :   
      fileWrite.write("[]")

# Récupération des valeurs depuis un fichier de données
print("Lecture des données depuis le fichier : " + fichierDATA)
with open(fichierDATA, 'r') as file :   
   data = json.load(file) 
file.close()

Now = datetime.datetime.now()
DateSonde = Now.strftime('%m-%d-%Y')
TimestanpSonde = Now.strftime('%I:%M')

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

############################################################
# Gestion du graphique
############################################################

# Chargement des données pour l'axe Y
for cle in data:
    #labels.append(pd.to_datetime(cle['heure'], format='%H:%M'))
    labels.append(cle['heure'])

# Chargement des données pour l'axe X
for cle in data:
    Tdr.append(cle['Tdr'])


# Calcul la moyenne totale depuis toutes les données
tabTdr = np.array(Tdr)
minTdr = np.min(Tdr)
maxTdr = np.max(Tdr)
moyTdf = np.mean(tabTdr) # Moyenne de toutes les données

# Mise en place du Titre du Graphique avec le host sondé
plt.title(host + "\n" + str(round(moyTdf)) + " ms " +  " - " + str(round(minTdr)) + " ms " + " - "+ str(round(maxTdr)) + " ms")

plt.plot([2000,2000])

# Graphique avec des petits traits et des bulles
plt.plot(labels,Tdr, marker='o', linestyle='dashed',markerfacecolor='green',linewidth=1)

# Nom des axes
plt.ylabel('Temps de réponse (ms)')
plt.xlabel('Heure')
#
ax = plt.gca()
#
## recompute the ax.dataLim
ax.relim()
## update ax.viewLim using the new dataLim
ax.autoscale_view()

# Affichage de la grille
plt.grid(True)  

# Sauvegarde en png avec un dpi de 300
plt.savefig(PrefixeDATA + SufixeGRAPH + ".png", dpi=300)  

plt.show()
#