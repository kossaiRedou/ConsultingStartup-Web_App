# Guide de Déploiement - GABITHEX sur fly.io

## Prérequis

1. Installation de flyctl
```bash
# Pour Windows (via PowerShell)
iwr https://fly.io/install.ps1 -useb | iex

# Pour MacOS/Linux
curl -L https://fly.io/install.sh | sh
```

2. Authentification
```bash
flyctl auth signup  # Pour créer un compte
# OU
flyctl auth login  # Si vous avez déjà un compte
```

## Configuration du Projet

1. Créer un `Dockerfile` à la racine du projet :
```dockerfile
FROM python:3.9-slim

# Variables d'environnement
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Répertoire de travail
WORKDIR /app

# Installation des dépendances système
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Installation des dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du projet
COPY . .

# Collecte des fichiers statiques
RUN python KOTO/manage.py collectstatic --noinput

# Exposition du port
EXPOSE 8000

# Commande de démarrage
CMD ["gunicorn", "--chdir", "KOTO", "KOTO.wsgi:application", "--bind", "0.0.0.0:8000"]
```

2. Créer un fichier `fly.toml` à la racine :
```toml
app = "gabithex"

[build]
  dockerfile = "Dockerfile"

[env]
  PORT = "8000"
  DJANGO_SETTINGS_MODULE = "KOTO.settings"

[http_service]
  internal_port = 8000
  force_https = true
  auto_stop_machines = true
  auto_start_machines = true
  min_machines_running = 0
  processes = ["app"]

[[statics]]
  guest_path = "/app/KOTO/staticfiles"
  url_prefix = "/static"
```

3. Mettre à jour `requirements.txt` avec les dépendances de production :
```
django
django-ckeditor
gunicorn
psycopg2-binary
whitenoise  # Pour la gestion des fichiers statiques
django-environ  # Pour la gestion des variables d'environnement
```

4. Configurer les variables d'environnement :
```bash
flyctl secrets set \
    DJANGO_SECRET_KEY="votre_clé_secrète" \
    DJANGO_DEBUG="False" \
    ALLOWED_HOSTS="gabithex.fly.dev" \
    DATABASE_URL="postgresql://..." \
    DJANGO_SETTINGS_MODULE="KOTO.settings"
```

## Configuration de la Base de Données

1. Créer une base de données PostgreSQL :
```bash
flyctl postgres create gabithex-db
```

2. Attacher la base de données à l'application :
```bash
flyctl postgres attach gabithex-db
```

## Déploiement

1. Lancer le déploiement initial :
```bash
flyctl launch
```

2. Appliquer les migrations :
```bash
flyctl ssh console -C "python KOTO/manage.py migrate"
```

3. Créer un superutilisateur :
```bash
flyctl ssh console -C "python KOTO/manage.py createsuperuser"
```

## Surveillance et Maintenance

1. Consulter les logs :
```bash
flyctl logs
```

2. Accéder à la console :
```bash
flyctl ssh console
```

3. Redémarrer l'application :
```bash
flyctl restart
```

## Points d'Attention

1. **Fichiers Statiques et Media**
   - Les fichiers statiques sont servis via WhiteNoise
   - Pour les fichiers media, configurer un service de stockage comme AWS S3 ou similaire

2. **Sécurité**
   - Vérifier que `DEBUG = False` en production
   - Utiliser des variables d'environnement pour les informations sensibles
   - Configurer correctement `ALLOWED_HOSTS`

3. **Performance**
   - Utiliser le cache Redis si nécessaire
   - Configurer la compression des réponses
   - Optimiser les requêtes de base de données

4. **Sauvegarde**
   - Configurer des sauvegardes automatiques de la base de données
   - Mettre en place une stratégie de restauration

## Mise à Jour de l'Application

Pour déployer des mises à jour :
```bash
flyctl deploy
```

## Rollback

En cas de problème après un déploiement :
```bash
flyctl deploy --image-label <version_précédente>
```

## Monitoring

1. Configurer Sentry pour le suivi des erreurs :
```python
# settings.py
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="votre-dsn-sentry",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
)
```

2. Mettre en place des alertes sur fly.io :
```bash
flyctl monitoring enable
```

## Support et Ressources

- Documentation fly.io : https://fly.io/docs/
- Documentation Django : https://docs.djangoproject.com/
- Support fly.io : https://community.fly.io/ 