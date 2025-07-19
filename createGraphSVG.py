
import numpy as np
from datetime import datetime
import json

class createGraph:
    fichierData = ""
    nomHost = ""
    dataGraph = []
    labels=[]
    Tdr=[]
    SufixeGRAPH = "_graph"
    PrefixeDATA = ""
    extensionGraph = "png"
    dpiGraph = 300
    enregistrementGraph =""
   
    def __init__(self, fichierJson, nomHost, enregistrementGraph = False):
        self.fichierData = fichierJson
        self.nomHost = nomHost
        self.enregistrementGraph = enregistrementGraph
        self.chargerData()
           
    def chargerData(self):
            # Récupération des valeurs depuis un fichier de données
            print("Lecture des données depuis le fichier : " + self.fichierData)
            with open(self.fichierData, 'r') as file :   
                self.dataGraph = json.load(file) 
            file.close()
            self.creationGraph()

    def time_to_seconds(self,time_str):
            minutes, seconds = time_str.split(':')
            return int(minutes) * 60 + int(seconds)

    def creationGraph(self):
        # Chargement des données pour l'axe Y
        for cle in self.dataGraph:
            self.labels.append(self.time_to_seconds(cle['heure']))
        print(self.labels)
        
        # Chargement des données pour l'axe X
        for cle in self.dataGraph:
            self.Tdr.append(cle['Tdr'])
        print(self.Tdr)
        # Calcul le min, le MAX et la moyenne totale
        tabTdr = np.array(self.Tdr)
        minTdr = np.min(self.Tdr)
        maxTdr = np.max(self.Tdr)
        moyTdf = np.mean(tabTdr)
        

nomfichierData = "myriamdupouycom_sondeSite.json"
nomduSite = "myriamdupouy.art"

# Chargement des données, création du graphique et enregistrement en local
testgraph = createGraph(nomfichierData, nomduSite, True)

print(testgraph.labels)

compteElement = len(testgraph.labels)

print("<svg height=\"1000\" width=\"1000\" xmlns=\"http://www.w3.org/2000/svg\">")


for i in range(compteElement):
    #print("x : " + str(testgraph.labels[i]) + " y: " + str(testgraph.Tdr[i]))
    print("<line x1=0 y1=0" + " x2=" + str(testgraph.labels[i]) + " y2=" + str(testgraph.Tdr[i]) + " style=\"stroke:red;stroke-width:2\" />")


#
#<svg height="200" width="300" xmlns="http://www.w3.org/2000/svg">
#  <line x1="0" y1="0" x2="300" y2="200" style="stroke:red;stroke-width:2" />
#</svg>


