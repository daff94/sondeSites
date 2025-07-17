from tinydb import TinyDB, Query
import datetime
import json

import matplotlib.pyplot as plt

db = TinyDB('sondeSite.json')

# Suppression de tout le contenu de la base de données
db.truncate()

Now = datetime.datetime.now()
DateSonde = Now.strftime('%d/%m/%Y')
TimestanpSonde = Now.strftime('%I:%M%p')

print(DateSonde)
print(TimestanpSonde)


db.insert ({'host':'myriamdupouy.com', 'Tdr':230, 'Status':200,'date':DateSonde,'heure':TimestanpSonde})
db.insert ({'host':'myriamdupouy.com', 'Tdr':540, 'Status':200,'date':DateSonde,'heure':TimestanpSonde})
db.insert ({'host':'myriamdupouy.com', 'Tdr':1230, 'Status':500,'date':DateSonde,'heure':TimestanpSonde})
db.insert ({'host':'myriamdupouy.com', 'Tdr':580, 'Status':200,'date':DateSonde,'heure':TimestanpSonde})
db.insert ({'host':'myriamdupouy.com', 'Tdr':344, 'Status':404,'date':DateSonde,'heure':TimestanpSonde})

for i in db:
    print(i)

# Récuépration des valeurs depuis la base TinyDB Json
with open('sondeSite.json', 'r') as file :   
   data = json.load(file) 

print(data)


#print(db.search(Query().date == '17/11/2025'))

# Gestion du graphique

labels = ['03:14', '043:14', '05:14', '06:14', '07:14']
Tdr = [230,540,1230,580,344]

plt.plot(labels,Tdr, marker='o', linestyle='dashed')

plt.ylabel('Temps de réponse (ms)')
plt.xlabel('Heure')

ax = plt.gca()

# recompute the ax.dataLim
ax.relim()
# update ax.viewLim using the new dataLim
ax.autoscale_view()
#plt.draw()

plt.show()

db.close