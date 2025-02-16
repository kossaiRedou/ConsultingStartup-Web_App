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

