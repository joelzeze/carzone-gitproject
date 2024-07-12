import psycopg2
import os
import django

# Initialiser les paramètres Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'carzone.settings')
django.setup()

connection = None

try:
    connection = psycopg2.connect(
        dbname='carzone_db',  # Remplacez par le nom de votre nouvelle base de données
        user='postgres',
        password='zovjsolange',
        host='localhost',
        port='5432'
    )
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print("Connexion réussie, version de la base de données :", db_version)
except Exception as error:
    print("Erreur de connexion :", error)
finally:
    if connection:
        connection.close()
