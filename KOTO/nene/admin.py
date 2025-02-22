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





#====================================================
#            Portfolio
#====================================
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Employee, Project, Technology, Experience, Education


class EducationInline(admin.TabularInline):  # Affichage en tableau
    model = Education
    extra = 1
    fields = ("degree", "specialty", "university", "start_date", "end_date", "city", "country")


class ExperienceInline(admin.TabularInline):  # Affichage en tableau
    model = Experience
    extra = 1
    fields = ("position", "company", "start_date", "end_date", "is_current", "city", "technologies")


class ProjectInline(admin.TabularInline):  # Affichage en tableau
    model = Project
    extra = 1
    fields = ("title", "slug", "description", "image", "technologies")


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "email", "phone", "location", "show_photo")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "email", "position", "location")
    list_filter = ("position", "location")
    
    # Organisation en sections pour une saisie fluide
    fieldsets = (
        ("👤 Informations Personnelles", {"fields": ("name", "slug", "email", "phone", "linkedin", "position", "photo", "location", "about")}),
    )

    inlines = [EducationInline, ExperienceInline, ProjectInline]  # Ajout des sections éducation, expérience et projets

    def show_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50" height="50" style="border-radius:50%;" />')
        return "No Image"
    show_photo.short_description = "Photo"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "employee", "show_image", "display_technologies")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "employee__name", "technologies__name")
    list_filter = ("technologies",)

    def show_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" style="border-radius:10%;" />')
        return "No Image"
    show_image.short_description = "Image"

    def display_technologies(self, obj):
        return ", ".join([tech.name for tech in obj.technologies.all()])
    display_technologies.short_description = "Technologies"


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("position", "company", "start_date", "end_date", "employee", "city")
    search_fields = ("position", "company", "employee__name", "city")
    list_filter = ("company", "start_date", "is_current")


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("specialty", "university", "start_date", "end_date", "employee", "city", "country")
    search_fields = ("specialty", "university", "employee__name", "city", "country")
    list_filter = ("university", "country", "start_date")
