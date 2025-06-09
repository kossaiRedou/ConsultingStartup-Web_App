FROM python:3.11-slim

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