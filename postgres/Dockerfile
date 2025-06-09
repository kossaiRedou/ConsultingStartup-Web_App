FROM postgres:15

# Configuration minimale pour Fly.io
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=gabithex

# Copier le fichier de configuration
COPY postgres.conf /etc/postgresql/postgresql.conf

# Exposition du port standard PostgreSQL
EXPOSE 5432

# Utiliser notre fichier de configuration
CMD ["postgres", "-c", "config_file=/etc/postgresql/postgresql.conf"] 