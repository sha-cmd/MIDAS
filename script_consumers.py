import random

import pandas as pd

from mimesis import Person, Datetime, Numeric
from mimesis.locales import Locale


# Création des générateurs de données
person = Person(locale=Locale.FR)
datetime = Datetime()
numeric = Numeric()

# Fonction pour générer un numéro de téléphone français
def generate_french_phone():
    return f"0{person.random.randint(1, 9)}{person.random.randint(10000000, 99999999):08d}"

# Fonction pour générer un numéro de carte de fidélité
def generate_loyalty_card():
    return f'FD{random.randint(100000, 999999)}'

# Génération des données
data = []
for i in range(1000):  # Génère 100 entrées
    prenom = person.first_name()
    nom = person.last_name()
    data.append({
        'id': i,
        'name': nom,
        'email': person.email(domains=('gmail.com', 'yahoo.fr', 'outlook.com')),
        'created_at': datetime.date(start=2020, end=2024),
    })

# Création d'un DataFrame pandas
df = pd.DataFrame(data)

# Affichage des 5 premières lignes
print(df.head())

# Sauvegarde des données dans un fichier CSV
df.to_csv('customers.csv', index=False)

