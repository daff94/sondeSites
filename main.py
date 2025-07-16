import requests
import time

# Debut du compteur
start = time.time()

# requete du get pour atteindre le site
r = requests.get('https://myriamdupouy.art')

# Fin du compter et affichage en ms
print(str(round((time.time() - start)*1000)) + " ms")

# Affichage du code retour de la commande "GET"
print(r.status_code)