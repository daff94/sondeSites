
import matplotlib.pyplot as plt
import numpy as np

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

    def creationGraph(self):
        # Chargement des données pour l'axe Y
        for cle in self.dataGraph:
            self.labels.append(cle['heure'])

        # Chargement des données pour l'axe X
        for cle in self.dataGraph:
            self.Tdr.append(cle['Tdr'])
        # Calcul la moyenne totale depuis toutes les données
        tabTdr = np.array(self.Tdr)
        minTdr = np.min(self.Tdr)
        maxTdr = np.max(self.Tdr)
        moyTdf = np.mean(tabTdr) # Moyenne de toutes les données

        # Mise en place du Titre du Graphique avec le host sondé
        plt.title(self.nomHost + "\n" + str(round(moyTdf)) + " ms " +  " - " + str(round(minTdr)) + " ms " + " - "+ str(round(maxTdr)) + " ms")

        # Affichage de la moyenne de l'ensemble des données
        plt.axhline(y=moyTdf, color='r', linestyle='--')

        # Graphique avec des petits traits et des bulles
        plt.plot(self.labels,self.Tdr, marker='o', linestyle='dashed',markerfacecolor='green',linewidth=1)

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
        if self.enregistrementGraph:
            plt.savefig(self.nomHost + self.SufixeGRAPH + "." + self.extensionGraph, dpi=self.dpiGraph)  

    def affichageGraph(self):
        # Affichage du graphique sur l'écran
        plt.show()


nomfichierData = "testkub_dev_sondeSite.json"
nonduSite = "testKup.dev.etat-ge.ch"

# Chargement des données, création du graphique et enregistrement en local
testgraph = createGraph(nomfichierData, nonduSite, True)

# Affichage du graphique représenté par l'objet "createGraph"
testgraph.affichageGraph()




