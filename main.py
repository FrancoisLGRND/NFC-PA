import requests
import getpass

def login_to_api(email, password):
    url = "http://localhost:80/api/nfc-writer/login"
    payload = {
        'email': email,
        'password': password
    }
    response = requests.post(url, data=payload)
    try:
        data = response.json()
        return data
    except ValueError:
        return None

def fetch_appartement(api_tokken, appartement_id):
    url = f"http://localhost:80/api/nfc-writer/tokken{appartement_id}"
    headers = {
        'Authorization': f'Bearer {api_tokken}'
    }
    response = requests.get(url, headers=headers)
    try:
        appartement_tokken = response.json()
        return appartement_tokken
    except ValueError:
        return None
    
""" email = input("Email : ")
password = getpass.getpass("Mot de passe : ") """
email = "lgrdpaco@gmail.com"
password = "Pommepomme1"
data = login_to_api(email, password)
if data:
    api_tokken = data['access_token']
    user = data['user']
else:
    print("Erreur login")

print(data)
appartement_id = input("Indiquez l'id de la propriété à relier avec le badge NFC : ")
appartement_tokken = fetch_appartement(api_tokken, appartement_id)
if appartement_tokken:
    print(appartement_tokken)
    # Ecrire sur le nfc ici
else:
    print("Id de propriété incorrecte")


# Requête à faire sur l'appli mobile pour update la date d'arrivé pour la réservation
url = f"http://localhost:80/api/nfc-update"
headers = {
        'Authorization': f'Bearer {api_tokken}'
    }

payload = {
        'appartement_tokken': appartement_tokken['appartement_tokken'],
    }
response = requests.put(url, headers=headers, data=payload)
try:
    appartement_tokken = response.json()
    print(appartement_tokken)
except ValueError:
    print("fail")