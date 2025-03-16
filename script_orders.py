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
n = 1000
for i in range(n):  # Génère 100 entrées
    prenom = person.first_name()
    nom = person.last_name()
    data.append({
        'id': i,
        'customer_id': random.randint(0,n),
        'order_date': datetime.date(start=2020, end=2024),
        'amount': round(numeric.decimal_number(start=10, end=1000),2),
        'status': random.choice(['Open', 'Closed']),
    })

# Création d'un DataFrame pandas
df = pd.DataFrame(data)

# Affichage des 5 premières lignes
print(df.head())

# Sauvegarde des données dans un fichier CSV
df.to_csv('orders.csv', index=False)


#os.system("gpg --encrypt --recipient romain@boyrie.email fausses_donnees_completes.csv")
#os.system("gpg --decrypt --recipient romain@boyrie.email fausses_donnees_completes.csv.gpg > data.csv")