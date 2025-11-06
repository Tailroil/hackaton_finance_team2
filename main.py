import os
from ibm_watson_machine_learning import APIClient
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

wml_credentials = {
    "apikey": os.getenv("API_KEY"),
    "url": os.getenv("IBM_URL")
}

client = APIClient(wml_credentials)

# Vérification de la connexion
print("Connexion établie avec Watsonx ✅")
print("Espace de déploiement disponibles :")
spaces = client.spaces.get_details()
for sp in spaces['resources']:
    print(f"- {sp['entity']['name']} ({sp['metadata']['id']})")
