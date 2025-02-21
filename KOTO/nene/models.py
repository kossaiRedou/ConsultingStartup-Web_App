from django.db import models

# Create your models here.

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
from django.db import models
from django.utils.text import slugify
from django.utils.safestring import mark_safe
import markdown

class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titre")
    slug = models.SlugField(unique=True, blank=True, verbose_name="Slug")
    author = models.CharField(max_length=100, verbose_name="Auteur")
    category = models.CharField(max_length=100, verbose_name="Catégorie")
    content = models.TextField(verbose_name="Contenu (Markdown)")  # Markdown pour le texte et le code
    image = models.ImageField(upload_to="articles/", verbose_name="Image", null=True, blank=True)
    published_date = models.DateField(auto_now_add=True, verbose_name="Date de publication")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Générer un slug à partir du titre
        super().save(*args, **kwargs)

    def render_markdown(self):
        """Convertit le Markdown en HTML avec coloration syntaxique."""
        return mark_safe(markdown.markdown(
            self.content,
            extensions=["fenced_code", "codehilite"]  # Active les blocs de code
        ))

    def __str__(self):
        return f"{self.title} - {self.author}"







#======================================================================
#                        Portfolio
#====================================================
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    position = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    location = models.CharField(max_length=100)
    about = models.TextField(max_length=1200)

    def __str__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    technologies = models.ManyToManyField(Technology, related_name='projects')

    def __str__(self):
        return f"{self.title} - {self.employee.name}"


class Experience(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='experiences')
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    is_current = models.BooleanField(default=False)  # Pour les postes actuels
    description = models.TextField(max_length=1200)
    technologies = models.ManyToManyField(Technology, related_name='experiences')
    city = models.CharField(max_length=100)

    class Meta:
        ordering = ['-start_date']  # Trier du plus récent au plus ancien


class Education(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=100, blank=True, null=True)  # Type de diplôme
    specialty = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    description = models.TextField(max_length=500)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    class Meta:
        ordering = ['-start_date']

