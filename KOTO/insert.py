import os
import django

# Initialiser Django (si le script est exécuté indépendamment)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KOTO.settings")  # Remplace 'myproject' par ton projet
django.setup()


from random import choice
from nene.models import Testimonial  # Remplace 'myapp' par le nom de ton application

# Liste de témoignages fictifs
testimonials_data = [
    {
        "name": "Marie Dupont",
        "feedback": "GABITHEX a transformé notre vision digitale en réalité. Une équipe exceptionnelle !",
        "company": "TechStart Solutions"
    },
    {
        "name": "Jean Martin",
        "feedback": "Développement web de qualité supérieure et accompagnement personnalisé. Je recommande vivement GABITHEX !",
        "company": "InnovateNow"
    },
    {
        "name": "Sophie Lambert",
        "feedback": "Application mobile parfaitement adaptée à nos besoins. L'équipe GABITHEX est très professionnelle.",
        "company": "MobileTech Pro"
    },
    {
        "name": "Alexandre Petit",
        "feedback": "Solutions IA innovantes qui ont révolutionné notre processus métier. Merci GABITHEX !",
        "company": "DataDriven Plus"
    },
    {
        "name": "Laura Fontaine",
        "feedback": "Transformation digitale réussie grâce à l'expertise technique de GABITHEX. Résultats exceptionnels !",
        "company": "DigitalTransform"
    },
    {
        "name": "Nicolas Rousseau",
        "feedback": "Service client remarquable et solutions techniques de pointe. GABITHEX dépasse nos attentes !",
        "company": None  # Pas d'entreprise spécifiée
    },
    {
        "name": "Élodie Garnier",
        "feedback": "Grâce à GABITHEX, notre plateforme web a atteint un niveau de performance inégalé.",
        "company": "WebExcellence"
    },
]

# Insérer les témoignages dans la base de données
for data in testimonials_data:
    if not Testimonial.objects.filter(name=data["name"], feedback=data["feedback"]).exists():
        testimonial = Testimonial(
            name=data["name"],
            feedback=data["feedback"],
            company=data["company"]
        )
        testimonial.save()
        print(f"Témoignage ajouté : {testimonial.name} - {testimonial.company if testimonial.company else 'Indépendant'}")
    else:
        print(f"Témoignage déjà existant : {data['name']}")

print("Insertion des témoignages terminée ! ✅")
