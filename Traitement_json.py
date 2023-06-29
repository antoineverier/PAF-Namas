import json
import shutil, os

## Sépare les photos malignes/bénines de la base de données ##

with open('Metadata_2018.json') as mon_fichier:
    data = json.load(mon_fichier)

files = os.listdir("ISIC_2018_TEST")

print(len(data))

for i in range(len(data)):
    if data[i]['benign_malignant'] == 'benign':
        shutil.move("ISIC_2018_TEST/" + data[i]["isic_id"] + ".JPG", "ISIC_2018/Benign" )
    if data[i]['benign_malignant'] == 'malignant':
        shutil.move("ISIC_2018_TEST/" + data[i]["isic_id"] + ".JPG", "ISIC_2018/Malignant" )
    else: 
        print("aucun des deux")
