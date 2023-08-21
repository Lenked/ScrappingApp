import requests
from bs4 import BeautifulSoup

url = input("Entrer l'URL du site : ")
response = requests.get(url)

if response.status_code == 200:
    html_content = response.content
else:
    print("Erreur lors de la récupération de la page.")

soup = BeautifulSoup(html_content, "html.parser")

# Extraire le titre de la page
title = soup.title.text
print("Titre de la page :", title)

# Élément de la page à extraire
element = input("Entrez l'élément a extraire du site : ")
elements = soup.find_all(f"{element}")
for item in elements:
    print(item)

# Exemple : Extraire tous les liens de la page
# links = soup.find_all("a")
# for link in links:
#    print(link.get("href"))
