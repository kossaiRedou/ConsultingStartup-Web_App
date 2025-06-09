from django.db import models
from django.utils.text import slugify
import itertools
from django.db import models
from django.utils.safestring import mark_safe
import markdown
import itertools
from django.utils.timezone import now
import markdown
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.timezone import now





class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom")
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(max_length=200, verbose_name="Sujet")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True)  # Date automatique

    def __str__(self):
        return f"{self.name} - {self.subject} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"





#===========================================
#                  Article
#==============================
class Article(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Brouillon'),
        ('published', 'Publié'),
    ]

    title = models.CharField(max_length=255, verbose_name="Titre")
    slug = models.SlugField(unique=True, blank=True, verbose_name="Slug")
    author = models.CharField(max_length=100, verbose_name="Auteur")
    category = models.CharField(max_length=100, verbose_name="Catégorie")
    content = RichTextUploadingField(verbose_name="Contenu")
    image = models.ImageField(upload_to="articles/", verbose_name="Image à la une", null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name="Statut")
    published_date = models.DateField(auto_now_add=True, verbose_name="Date de publication")
    meta_description = models.CharField(max_length=160, blank=True, help_text="Description pour le SEO", verbose_name="Meta description")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ['-published_date']

    def __str__(self):
        return f"{self.title} - {self.author}"







#======================================================================
#                        Portfolio
#====================================================

class SoftSkills(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    linkedin = models.URLField(blank=True, null=True)
    gitHub = models.URLField(blank=True, null=True)
    medium = models.URLField(blank=True, null=True)

    position = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    location = models.CharField(max_length=100)

    about = models.TextField(max_length=1200, null=True)
    softSkills = models.ManyToManyField(SoftSkills, related_name='employees')
    cv = models.FileField(upload_to='KOTO/media/cvs', blank=True, null=True)  # Ajout du champ CV

    def save(self, *args, **kwargs):
        # Vérifier si l'objet est nouveau ou si le nom a changé
        if not self.pk or not self.slug.startswith(slugify(self.name)):
            base_slug = slugify(self.name, allow_unicode=True).replace("-", "_")
            slug = base_slug

            for i in itertools.count(1):
                if not Employee.objects.filter(slug=slug).exclude(id=self.id).exists():
                    break
                slug = f"{base_slug}_{i}"

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name





class Technology(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name





class Project(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Brouillon'),
        ('in_progress', 'En cours'),
        ('completed', 'Terminé'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='projects', verbose_name="Employé")
    title = models.CharField(max_length=200, verbose_name="Titre")
    slug = models.SlugField(unique=True, blank=True, verbose_name="Slug")

    date = models.DateField(default=now, verbose_name="Date")
    description = RichTextUploadingField(verbose_name="Description")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress', verbose_name="Statut")

    image = models.ImageField(upload_to='projects/', blank=True, null=True, verbose_name="Image principale")
    technologies = models.ManyToManyField(Technology, related_name='projects', verbose_name="Technologies")

    demo = models.URLField(blank=True, null=True, verbose_name="Lien de démonstration")
    depot = models.URLField(blank=True, null=True, verbose_name="Dépôt de code")
    
    meta_description = models.CharField(max_length=160, blank=True, help_text="Description pour le SEO", verbose_name="Meta description")

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            for i in itertools.count(1):
                if not Project.objects.filter(slug=slug).exists():
                    break
                slug = f"{base_slug}_{i}"
            self.slug = slug
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"
        ordering = ['-date']

    def __str__(self):
        return f"{self.title} - {self.employee.name}"


class Experience(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='experiences')
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(max_length=1200)
    technologies = models.ManyToManyField(Technology, related_name='experiences')
    city = models.CharField(max_length=100)

    class Meta:
        ordering = ['-start_date']


    def save(self, *args, **kwargs):
        # Enregistrer d'abord l'expérience
        super().save(*args, **kwargs)

        # Si cette expérience est marquée comme étant "actuelle"
        if self.is_current:
            employee = self.employee
            # Mise à jour de la position et de la location de l'employé
            employee.position = self.position
            employee.location = self.city
            # Sauvegarde de l'employé avec les nouvelles informations
            employee.save(update_fields=['position', 'location'])



    def __str__(self):
        end_date_display = self.end_date.strftime("%Y") if self.end_date else "En cours"
        return f"{self.position} at {self.company} ({end_date_display})"




class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Certification(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='certifications')
    title = models.CharField(max_length=150)  # Titre de la certification
    platform = models.CharField(max_length=100)  # Plateforme délivrant la certif (Udemy, Coursera...)
    link = models.URLField(blank=True, null=True)  # Lien vers la certification
    image = models.ImageField(upload_to='certifications/', blank=True, null=True)  # Image de la certification
    skills = models.ManyToManyField(Skill, related_name='certifications')  # Compétences acquises
    date = models.DateField(default=now)

    class Meta:
        ordering = ['-date']  # Tri par date décroissante (du plus récent au plus ancien)

    def __str__(self):
        return f"{self.title} - {self.platform}"














class Education(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=100, blank=True, null=True)
    specialty = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(max_length=500)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        end_date_display = self.end_date.strftime("%Y") if self.end_date else "En cours"
        return f"{self.specialty} - {self.university} ({end_date_display})"





#================================================
#            Section About
#===================================
class AboutSection(models.Model):
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    history_title = models.CharField(max_length=255)
    history_text = models.TextField()
    mission = models.TextField(default=None)  # <== Assure-toi que ce champ existe bien !
    image = models.ImageField(upload_to="about_images/", null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)



    def __str__(self):
        return self.title



#========================================================
#                   SERVICES
#========================================

class Service(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Titre du service"
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
        null=True,
        #editable=False
    )
    short_description = models.CharField(
        max_length=255,
        null=True,
        verbose_name="Description courte",
        help_text="Une phrase percutante qui résume le service."
    )
    detailed_description = models.TextField(
        null=True,
        verbose_name="Description complète",
        help_text="Explique en quoi ce service est utile et ses avantages."
    )
    benefits = models.TextField(
        null=True,
        verbose_name="Avantages clés",
        help_text="Liste des bénéfices concrets, séparés par des virgules."
    )
    target_clients = models.CharField(
        max_length=255,
        null=True,
        verbose_name="Public cible",
        help_text="Ex: Startups, PME, Grandes entreprises, Freelancers..."
    )
    image = models.ImageField(
        upload_to="services/",
        blank=True,
        null=False,
        verbose_name="Image illustrant le service"
    )
    call_to_action = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Texte d'appel à l'action",
        help_text="Ex: Contactez-nous pour une consultation gratuite"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date de création"
    )

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['created_at']  # Optionnel, pour trier les services par date de création

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            unique_slug = base_slug
            counter = 1
            while Service.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)



class Testimonial(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nom du client")
    feedback = models.TextField(verbose_name="Témoignage")
    company = models.CharField(max_length=255, null=True, blank=True, verbose_name="Entreprise (optionnel)")
    position = models.CharField(max_length=255, null=True, blank=True, verbose_name="Poste occupé")
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Témoignage"
        verbose_name_plural = "Témoignages"

    def __str__(self):
        position_info = f" - {self.position}" if self.position else ""
        company_info = f" ({self.company})" if self.company else ""
        return f"{self.name}{position_info}{company_info}"









# Nos pratiques:
class Practice(models.Model):
    number = models.PositiveIntegerField(verbose_name="Numéro", unique=True)  # Empêche les doublons
    title = models.CharField(max_length=255, verbose_name="Titre")
    description = models.TextField(verbose_name="Description")

    class Meta:
        ordering = ['number']
        verbose_name = "Pratique"
        verbose_name_plural = "Nos Pratiques"

    def formatted_number(self):
        """Retourne le numéro formaté avec deux chiffres (ex: 02, 03, 10)"""
        return f"{self.number:02d}"

    def __str__(self):
        """Affichage propre dans Django Admin et autres vues"""
        return f"{self.formatted_number()}. {self.title}"



#========================================================
#                   Customers
#========================================

class Customer(models.Model):
    SECTEURS_CHOICES = [
        ('tech', 'Technologie'),
        ('finance', 'Finance'),
        ('sante', 'Santé'),
        ('ecommerce', 'E-commerce'),
        ('industrie', 'Industrie'),
        ('autre', 'Autre'),
    ]

    nom = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='clients/')
    secteur = models.CharField(max_length=50, choices=SECTEURS_CHOICES, default='autre')

    def __str__(self):
        return f"{self.nom} - {self.get_secteur_display()}"




#=========================================
# Carousel items
#=====================
class HeroCarousel(models.Model):
    image = models.ImageField(upload_to='hero-carousel/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)  # Permet de trier les éléments du carrousel

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']  # Trier les éléments du carrousel par ordre croissant


#=========================================
# Conversion Stats
#=====================
class ConversionStats(models.Model):
    """Modèle pour gérer les statistiques affichées sur le site pour améliorer la conversion"""
    
    projects_completed = models.PositiveIntegerField(
        default=50, 
        verbose_name="Projets Réalisés",
        help_text="Nombre total de projets terminés"
    )
    
    client_satisfaction = models.PositiveIntegerField(
        default=98, 
        verbose_name="Satisfaction Client (%)",
        help_text="Pourcentage de satisfaction client"
    )
    
    response_time_hours = models.PositiveIntegerField(
        default=24, 
        verbose_name="Temps de Réponse (heures)",
        help_text="Temps de réponse maximum en heures"
    )
    
    years_experience = models.PositiveIntegerField(
        default=5, 
        verbose_name="Années d'Expérience",
        help_text="Nombre d'années d'expertise"
    )
    
    active_clients = models.PositiveIntegerField(
        default=30, 
        verbose_name="Clients Actifs",
        help_text="Nombre de clients actuellement accompagnés"
    )
    
    technologies_mastered = models.PositiveIntegerField(
        default=15, 
        verbose_name="Technologies Maîtrisées",
        help_text="Nombre de technologies et frameworks maîtrisés"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(
        default=True,
        verbose_name="Actif",
        help_text="Utiliser ces statistiques sur le site"
    )
    
    class Meta:
        verbose_name = "Statistiques de Conversion"
        verbose_name_plural = "Statistiques de Conversion"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Stats du {self.created_at.strftime('%d/%m/%Y')}"
    
    @classmethod
    def get_active_stats(cls):
        """Retourne les statistiques actives pour l'affichage"""
        return cls.objects.filter(is_active=True).first() or cls.objects.create()


#=========================================
# Pricing Plans for Conversion
#=====================
class PricingPlan(models.Model):
    """Plans tarifaires pour améliorer la conversion"""
    
    PLAN_TYPES = [
        ('starter', 'Starter'),
        ('professional', 'Professionnel'),
        ('enterprise', 'Entreprise'),
        ('custom', 'Sur Mesure'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Nom du Plan")
    plan_type = models.CharField(max_length=20, choices=PLAN_TYPES, default='starter')
    
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Prix (€)",
        help_text="Prix en euros"
    )
    
    price_period = models.CharField(
        max_length=50, 
        default="projet",
        verbose_name="Période",
        help_text="Ex: projet, mois, an"
    )
    
    description = models.TextField(verbose_name="Description du plan")
    
    features = models.TextField(
        verbose_name="Fonctionnalités",
        help_text="Une fonctionnalité par ligne"
    )
    
    is_popular = models.BooleanField(
        default=False,
        verbose_name="Plan Populaire",
        help_text="Mettre en avant ce plan"
    )
    
    is_active = models.BooleanField(default=True, verbose_name="Actif")
    
    order = models.PositiveIntegerField(default=0, verbose_name="Ordre d'affichage")
    
    cta_text = models.CharField(
        max_length=100, 
        default="Démarrer",
        verbose_name="Texte du bouton"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Plan Tarifaire"
        verbose_name_plural = "Plans Tarifaires"
        ordering = ['order', 'price']
    
    def __str__(self):
        return f"{self.name} - {self.price}€"
    
    def get_features_list(self):
        """Retourne la liste des fonctionnalités"""
        return [feature.strip() for feature in self.features.split('\n') if feature.strip()]


#=========================================
# Lead Capture
#=====================
class Lead(models.Model):
    """Modèle pour capturer les leads via différents formulaires"""
    
    LEAD_SOURCES = [
        ('contact_form', 'Formulaire de Contact'),
        ('newsletter', 'Newsletter'),
        ('free_consultation', 'Consultation Gratuite'),
        ('pricing_page', 'Page Tarifs'),
        ('service_page', 'Page Service'),
        ('blog', 'Blog'),
        ('other', 'Autre'),
    ]
    
    LEAD_STATUS = [
        ('new', 'Nouveau'),
        ('contacted', 'Contacté'),
        ('qualified', 'Qualifié'),
        ('proposal_sent', 'Devis Envoyé'),
        ('won', 'Gagné'),
        ('lost', 'Perdu'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Nom")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Téléphone")
    company = models.CharField(max_length=100, blank=True, null=True, verbose_name="Entreprise")
    
    project_type = models.CharField(max_length=100, blank=True, null=True, verbose_name="Type de Projet")
    budget_range = models.CharField(max_length=50, blank=True, null=True, verbose_name="Budget")
    timeline = models.CharField(max_length=50, blank=True, null=True, verbose_name="Délai")
    
    message = models.TextField(blank=True, null=True, verbose_name="Message")
    
    source = models.CharField(
        max_length=20, 
        choices=LEAD_SOURCES, 
        default='contact_form',
        verbose_name="Source"
    )
    
    status = models.CharField(
        max_length=20, 
        choices=LEAD_STATUS, 
        default='new',
        verbose_name="Statut"
    )
    
    is_urgent = models.BooleanField(default=False, verbose_name="Urgent")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Dernière mise à jour")
    
    # Tracking pour conversion
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    referrer = models.URLField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Lead"
        verbose_name_plural = "Leads"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.email} ({self.get_status_display()})"


class CodeSnippet(models.Model):
    LANGUAGE_CHOICES = [
        ('python', 'Python'),
        ('javascript', 'JavaScript'),
        ('html', 'HTML'),
        ('css', 'CSS'),
        ('php', 'PHP'),
        ('java', 'Java'),
        ('sql', 'SQL'),
        ('bash', 'Bash'),
        ('other', 'Autre'),
    ]
    
    article = models.ForeignKey(Article, related_name='code_snippets', on_delete=models.CASCADE, verbose_name="Article")
    title = models.CharField(max_length=100, verbose_name="Titre")
    code = models.TextField(verbose_name="Code")
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES, verbose_name="Langage")
    
    class Meta:
        verbose_name = "Extrait de code"
        verbose_name_plural = "Extraits de code"
        ordering = ['id']

    def __str__(self):
        return f"{self.title} ({self.language})"
