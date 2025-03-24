# Fodor-Analytics Startup - Web Application

## Description
Kossairedou Consulting Startup Web App est une application web développée avec Django. Elle est conçue pour gérer et afficher des informations sur les services, les clients, les projets, les témoignages et bien plus encore. Cette application est développée avec une approche dynamique et modulaire, permettant à l'administrateur de modifier tous les éléments (contenu) depuis l'espace admin.

## Fonctionnalités
- Gestion des services offerts par l'entreprise
- Présentation des projets réalisés
- Gestion des témoignages clients
- Carrousel dynamique pour la page d'accueil
- Administration via Django Admin
- Rédaction d'articles de blog
- Gestion du portfolio pour les membres de l'équipe

## Structure du projet
Le projet est organisé comme suit :


kossairedou-consultingstartup-web_app/
│── KOTO/
│   ├── db.sqlite3
│   ├── insert.py
│   ├── manage.py
│   ├── requirements.txt
│   ├── KOTO/  # Configuration principale du projet Django
│   ├── media/  # Stockage des fichiers médias (images, CV, etc.)
│   ├── nene/   # Application principale de l'entreprise
│   ├── static/  # Fichiers statiques (CSS, JS, images)
│   ├── staticfiles/  # Fichiers collectés pour le déploiement


## Prérequis

Pour réussir, assurez-vous d'avoir des connaissances en programmation Python et en langages front-end comme HTML, CSS et Bootstrap 5.

- Python 3.12
- Django
- Bootstrap

## Installation et exécution

1. Clonez le dépôt :

   ```sh
   git clone <lien-du-repo>
   cd kossairedou-consultingstartup-web_app/KOTO/
   ```

2. Créez un environnement virtuel et activez-le :

   ```sh
   python -m venv env
   source env/bin/activate  # Sur macOS/Linux
   env\Scripts\activate  # Sur Windows
   ```

3. Installez les dépendances :

   ```sh
   pip install -r requirements.txt
   ```

4. Appliquez les migrations :

   ```sh
   python manage.py migrate
   ```

5. Démarrez le serveur :

   ```sh
   python manage.py runserver
   ```

L'application sera accessible sur `http://127.0.0.1:8000/`

## Administration Django
Pour accéder à l'interface d'administration :

1. Créez un superutilisateur :
   ```sh
   python manage.py createsuperuser
   ```
2. Connectez-vous à l'interface d'administration via `http://127.0.0.1:8000/admin/`.

## Déploiement
Pour déployer l'application sur un serveur, choisissez la solution qui correspond le mieux à vos besoins.

## Auteur
Développé par (Aliou DIALLO) Kossairedou

## Licence
Ce projet est sous licence MIT.

