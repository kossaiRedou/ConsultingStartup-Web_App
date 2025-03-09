import os
import django
from django.utils.text import slugify

# Configurer Django pour exécuter ce script indépendamment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KOTO.settings")  # Remplace "KOTO" par ton projet Django
django.setup()

from nene.models import Service  # Vérifie que "nene" est bien ton application Django

# Liste des services à insérer
services = [
    {
        "title": "Analyse des tendances sectorielles",
        "short_description": "Anticipez les tendances du marché avant vos concurrents.",
        "detailed_description": "Nous vous aidons à identifier les évolutions du marché grâce à une veille stratégique et une analyse approfondie des tendances émergentes.",
        "benefits_list": ["Anticipation des tendances", "Réduction des risques", "Prise de décision éclairée"],
        "target_clients_list": ["Entreprises technologiques", "Startups innovantes", "PME"],
        "call_to_action": "Demandez votre analyse gratuite dès aujourd’hui.",
        "image": "services/analyse.jpg"
    },
    {
        "title": "Veille concurrentielle",
        "short_description": "Gardez un œil sur vos concurrents et adaptez votre stratégie.",
        "detailed_description": "Nous mettons en place des outils avancés de veille pour suivre l’évolution de vos concurrents et identifier les opportunités du marché.",
        "benefits_list": ["Détection des menaces", "Positionnement stratégique", "Amélioration de l'offre"],
        "target_clients_list": ["Entreprises de tous secteurs", "E-commerçants", "Consultants"],
        "call_to_action": "Obtenez votre rapport de veille concurrentielle.",
        "image": "services/veille.jpg"
    },
    {
        "title": "Visualisation des données et Dashboards",
        "short_description": "Transformez vos données en décisions stratégiques.",
        "detailed_description": "Nous créons des tableaux de bord interactifs (Power BI, SAS Viya) pour vous permettre de suivre vos indicateurs clés en temps réel.",
        "benefits_list": ["Meilleure compréhension des données", "Reporting automatisé", "Décisions basées sur les faits"],
        "target_clients_list": ["Directeurs financiers", "Responsables marketing", "Data Analysts"],
        "call_to_action": "Découvrez nos solutions de visualisation sur mesure.",
        "image": "services/dashboard.jpg"
    },
    {
        "title": "Études de marché et segmentation",
        "short_description": "Comprenez votre marché et ciblez efficacement vos clients.",
        "detailed_description": "Nous réalisons des études approfondies et des segmentations clients avancées pour vous aider à maximiser vos performances commerciales.",
        "benefits_list": ["Meilleur ciblage client", "Stratégie optimisée", "Connaissance approfondie du marché"],
        "target_clients_list": ["Entreprises souhaitant se développer", "Startups en lancement", "Services marketing"],
        "call_to_action": "Planifiez une consultation pour une étude personnalisée.",
        "image": "services/segmentation.jpg"
    },
    {
        "title": "Développement d’applications Web",
        "short_description": "Des solutions web performantes et évolutives pour votre entreprise.",
        "detailed_description": "Nous développons des applications web sur mesure en utilisant Django et Python pour automatiser vos processus et optimiser la gestion de vos données.",
        "benefits_list": ["Sites rapides et sécurisés", "Développement sur mesure", "Maintenance simplifiée"],
        "target_clients_list": ["Entreprises de toutes tailles", "Startups tech", "Plateformes SaaS"],
        "call_to_action": "Obtenez un devis pour votre projet web.",
        "image": "services/dev-web.jpg"
    },
    {
        "title": "Web Scraping et écoute stratégique",
        "short_description": "Exploitez la puissance des données web pour prendre l’avantage.",
        "detailed_description": "Nous collectons des données stratégiques sur le web pour affiner vos décisions et surveiller l’évolution de votre marché en temps réel.",
        "benefits_list": ["Accès à des données précieuses", "Suivi en temps réel", "Automatisation de la veille"],
        "target_clients_list": ["Analystes", "Investisseurs", "Agences de veille stratégique"],
        "call_to_action": "Démarrez votre projet de Web Scraping avec nous.",
        "image": "services/scraping.jpg"
    },
]

# Insérer les données en base
for service in services:
    # Générer un slug unique
    base_slug = slugify(service["title"])
    unique_slug = base_slug
    counter = 1
    while Service.objects.filter(slug=unique_slug).exists():
        unique_slug = f"{base_slug}-{counter}"
        counter += 1

    service["slug"] = unique_slug  # Ajouter le slug généré

    # Vérifier si le service existe déjà, sinon l'insérer
    obj, created = Service.objects.update_or_create(
        title=service["title"],
        defaults={
            "slug": service["slug"],
            "short_description": service["short_description"],
            "detailed_description": service["detailed_description"],
            "benefits_list": service["benefits_list"],
            "target_clients_list": service["target_clients_list"],
            "call_to_action": service["call_to_action"],
            "image": service["image"],
        }
    )

    if created:
        print(f"✅ Service ajouté : {service['title']} (slug: {service['slug']})")
    else:
        print(f"♻️ Service mis à jour : {service['title']}")

print("🎉 Insertion terminée !")
