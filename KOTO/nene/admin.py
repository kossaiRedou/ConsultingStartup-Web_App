from django.contrib import admin
from .models import Contact
from django.contrib import admin
from django.utils.html import format_html
from .models import Article, Skill



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
    extra = 0
    fields = ("degree", "specialty", "university", "start_date", "end_date", "city", "country")


class ExperienceInline(admin.TabularInline):  # Affichage en tableau
    model = Experience
    extra = 0
    fields = ("position", "company", "start_date", "end_date", "is_current", "city", "technologies")


class ProjectInline(admin.TabularInline):  # Affichage en tableau
    model = Project
    extra = 0
    fields = ("title", "slug", "description", "image", "technologies")


from .models import Employee, Project, Technology, Experience, Education, SoftSkills, Certification

class CertificationInline(admin.TabularInline):  
    model = Certification  
    extra = 0 
    fields = ("title", "platform", "link", "image", "skills")




# Mise à jour de l'admin Employee pour inclure les certifications
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "email", "phone", "location", "show_photo", "display_soft_skills")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "email", "position", "location", "softSkills__name")
    list_filter = ("position", "location", "softSkills")

    fieldsets = (
        ("👤 Informations Personnelles", {
            "fields": ("name", "slug", "email", "phone", "linkedin", "gitHub", "medium", "position", "photo", "cv", "location", "about", "softSkills"),
        }),
    )

    filter_horizontal = ("softSkills",)
    inlines = [EducationInline, ExperienceInline, ProjectInline, CertificationInline]  # Ajout des certifications ici !

    def show_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50" height="50" style="border-radius:50%;" />')
        return "No Image"
    show_photo.short_description = "Photo"

    def display_soft_skills(self, obj):
        return ", ".join([skill.name for skill in obj.softSkills.all()])
    display_soft_skills.short_description = "Soft Skills"


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


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("title", "platform", "employee", "show_image", "display_skills")
    search_fields = ("title", "platform", "employee__name", "skills__name")
    list_filter = ("platform",)
    filter_horizontal = ("skills",)

    def show_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" style="border-radius:10%;" />')
        return "No Image"
    show_image.short_description = "Image"

    def display_skills(self, obj):
        return ", ".join([skill.name for skill in obj.skills.all()])
    display_skills.short_description = "Compétences acquises"


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
