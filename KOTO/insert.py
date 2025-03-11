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
        "feedback": "Service impeccable, rapide et professionnel. Je recommande fortement !",
        "company": "Digital Solutions"
    },
    {
        "name": "Jean Martin",
        "feedback": "Une équipe à l'écoute et des résultats impressionnants. Un vrai partenaire de confiance !",
        "company": "StartupBoost"
    },
    {
        "name": "Sophie Lambert",
        "feedback": "Très satisfaite, j’ai enfin trouvé une solution adaptée à mes besoins.",
        "company": "Marketing Pro"
    },
    {
        "name": "Alexandre Petit",
        "feedback": "Des conseils avisés et un accompagnement sur-mesure. Merci pour votre aide !",
        "company": "E-commerce Plus"
    },
    {
        "name": "Laura Fontaine",
        "feedback": "Des experts en stratégie digitale ! Mon entreprise a vu ses performances exploser.",
        "company": "WebInnov"
    },
    {
        "name": "Nicolas Rousseau",
        "feedback": "Un service client au top ! Réactif et efficace. Je recommande sans hésiter.",
        "company": None  # Pas d'entreprise spécifiée
    },
    {
        "name": "Élodie Garnier",
        "feedback": "Grâce à eux, j’ai optimisé ma stratégie commerciale et boosté mes ventes.",
        "company": "Consulting Experts"
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
