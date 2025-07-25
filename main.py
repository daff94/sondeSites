
import time
import requests

http_proxy  = "http://127.0.0.1:3128"
https_proxy = "http://127.0.0.1:3128"
ftp_proxy   = "ftp://127.0.0.1:3128"

proxies = { 
              "http"  : http_proxy, 
              "https" : https_proxy, 
              "ftp"   : ftp_proxy
            }

def pingsite(hostanalyse):
    debut = time.time()
    r = requests.get(hostanalyse, proxies=proxies, verify='FiddlerRoot.pem')
    fin = time.time()
    duree = round((fin - debut)*1000) 
    print("Temps de réponse du site : " + hostanalyse + " - " + str(duree) + "ms")



host = "https://cis-report.apps.soca.lbdev.etat-ge.ch"
hostext = "https://www.myriamdupouy.art"
hostssl = "https://github.com"


pingsite(hostssl)
pingsite(hostext)
pingsite(host)
