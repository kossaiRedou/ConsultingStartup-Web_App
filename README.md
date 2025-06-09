# GABITHEX - Web Application

## Description
GABITHEX Web App est une application web développée avec Django. Elle est conçue pour gérer et afficher des informations sur les services, les clients, les projets, les témoignages et bien plus encore. Cette application est développée avec une approche dynamique et modulaire, permettant à l'administrateur de modifier tous les éléments (contenu) depuis l'espace admin.

## Aperçu
### Capture d'écran du site 🔗 **Lien vers le site :** [GABITHEX Consulting Web App](https://www.gabithex.fr/)

![Capture d'écran du site](KOTO/media/site.png)

### Diagramme de la base de données
![Diagramme de la base de données](KOTO/media/gabithex-Analytics.png)




## Fonctionnalités
- Gestion des services offerts par l'entreprise
- Présentation des projets réalisés
- Gestion des témoignages clients
- Carrousel dynamique pour la page d'accueil
- Administration via Django Admin
- Rédaction d'articles de blog
- Gestion du portfolio pour les membres de l'équipe

## Structure du projet
Le projet est organisé comme suit [Structure hiérarchique du projet Django](https://gitingest.com/kossaiRedou/ConsultingStartup-Web_App)

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

## Licence

Ce projet est sous licence MIT.

## 🚀 Déploiement sur Fly.io (100% Gratuit)

Ce guide explique comment déployer l'application et sa base de données PostgreSQL sur Fly.io en restant dans les limites gratuites.

### Prérequis

1. Un compte Fly.io
2. [flyctl](https://fly.io/docs/hands-on/install-flyctl/) installé
3. Un token GitHub pour les actions (pour le déploiement automatique)

### Structure du Déploiement

- Application Django : 1 VM gratuite
- Base PostgreSQL : Volume de 3 Go (gratuit)
- Pas d'utilisation de Fly Postgres (payant)

### 1. Déploiement de la Base PostgreSQL

```bash
# Dans le dossier postgres/
flyctl apps create mon-postgres
flyctl volumes create pg_data --size 3 --region cdg
flyctl deploy
```

Notez l'URL interne : `mon-postgres.internal:5432`

### 2. Configuration de l'Application Django

1. Configurer les secrets :
```bash
flyctl secrets set \
  DATABASE_URL="postgresql://postgres:postgres@mon-postgres.internal:5432/gabithex" \
  DJANGO_SECRET_KEY="votre-clé-secrète" \
  DJANGO_DEBUG="False"
```

2. Déployer l'application :
```bash
flyctl apps create gabithex
flyctl deploy
```

### 3. Configuration du Déploiement Automatique

1. Dans GitHub, ajoutez le secret `FLY_API_TOKEN`
2. Activez les GitHub Actions dans votre dépôt
3. Poussez sur la branche main pour déclencher le déploiement

### 🔒 Variables d'Environnement

- `DATABASE_URL` : URL de connexion PostgreSQL
- `DJANGO_SECRET_KEY` : Clé secrète Django
- `DJANGO_DEBUG` : "False" en production
- `DJANGO_SETTINGS_MODULE` : "KOTO.settings"

### 📦 Limites Gratuites Fly.io

- 3 machines partagées de 256 MB RAM
- 3 GB de volume persistant
- 160 GB de transfert sortant

### 🔍 Surveillance

```bash
# Logs de l'application
flyctl logs

# Status des applications
flyctl status

# Console PostgreSQL
flyctl postgres connect -a mon-postgres
```

### ⚠️ Points d'Attention

1. **Base de données** :
   - Sauvegardez régulièrement
   - Limitez la taille à 3 GB (limite gratuite)

2. **Performance** :
   - Utilisez le cache
   - Optimisez les requêtes
   - Compressez les réponses

3. **Sécurité** :
   - `DEBUG=False` en production
   - Utilisez HTTPS (activé par défaut)
   - Protégez les secrets

### 🆘 Dépannage

1. **Problèmes de connexion DB** :
   - Vérifiez l'URL interne
   - Testez la connexion : `flyctl postgres connect`

2. **Erreurs de déploiement** :
   - Vérifiez les logs : `flyctl logs`
   - Validez les secrets : `flyctl secrets list`

### 📚 Documentation

- [Fly.io Documentation](https://fly.io/docs/)
- [Django Documentation](https://docs.djangoproject.com/)
- [GitHub Actions](https://docs.github.com/en/actions)
