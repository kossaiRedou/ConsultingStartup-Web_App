from django.contrib import admin
from .models import Contact
from django.contrib import admin
from django.utils.html import format_html
from .models import Article


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")  # Colonnes visibles
    search_fields = ("name", "email", "subject")  # Barre de recherche
    list_filter = ("created_at",)  # Filtres sur la date
    ordering = ("-created_at",)  # Tri par date décroissante






# Article
from django.contrib import admin
from django.utils.html import format_html
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "published_date")
    search_fields = ("title", "author", "category")
    list_filter = ("category", "published_date")
    ordering = ("-published_date",)
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("published_date", "preview_markdown")  # Empêche toute modification

    fieldsets = (
        ("Informations Générales", {
            "fields": ("title", "slug", "author", "category"),
        }),
        ("Contenu", {
            "fields": ("content", "preview_markdown"),
        }),
        ("Publication", {
            "fields": ("published_date",),  # Affiché en lecture seule
        }),
    )

    def preview_markdown(self, obj):
        """Affiche un aperçu du contenu Markdown converti en HTML"""
        return format_html(obj.render_markdown())

    preview_markdown.short_description = "Aperçu du Markdown"
