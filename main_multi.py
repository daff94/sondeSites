
import time
import requests

import threading

http_proxy  = "http://127.0.0.1:3128"
https_proxy = "http://127.0.0.1:3128"
ftp_proxy   = "ftp://127.0.0.1:3128"

proxies = { 
              "http"  : http_proxy, 
              "https" : https_proxy, 
              "ftp"   : ftp_proxy
            }

def pingsite(hostanalyse):
    print("Sonde sur  " + hostanalyse + " en cours...")
    debut = time.time()
    r = requests.get(hostanalyse, proxies=proxies, verify='FiddlerRoot.pem')
    fin = time.time()
    duree = round((fin - debut)*1000) 
    print("Temps de réponse du site : " + hostanalyse + " - " + str(duree) + "ms.")


host = "https://cis-report.apps.soca.lbdev.etat-ge.ch"
hostext = "https://www.myriamdupouy.art"
hostssl = "https://github.com"


# Créer et démarrer les threads
thread1 = threading.Thread(target=pingsite, args=(host,))
thread2 = threading.Thread(target=pingsite, args=(hostext,))

print("Démarrage des sondes ...")
thread1.start()
thread2.start()

# Attendre la fin des threads
thread1.join()
thread2.join()

print("Fin.")
