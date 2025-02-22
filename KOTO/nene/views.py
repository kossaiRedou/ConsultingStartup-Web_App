from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from django.utils.timezone import now
from .models import Employee, Education, Experience, Project, Technology, Certification, Article




def index(request):
    return render(request, 'nene/index.html', {"timestamp": now().timestamp()})

#==============================================================
#        About
#==============================================
def about(request):
    employees = Employee.objects.all()  # Récupérer tous les employés
    return render(request, 'nene/about.html', {"employees": employees})



#==================================================
#                   Blog
#====================================
def blog(request):
    articles = Article.objects.all().order_by("-published_date")  # Trier du plus récent au plus ancien
    return render(request, "nene/blog.html", {"articles": articles})




def blog_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, "nene/blog_details.html", {"article": article})




#=============================================
#         CONTACT VIEW
#=================================================
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()  # Enregistre en base de données

            # Envoyer un email (facultatif)
            send_mail(
                f"Message de {contact.name} - {contact.subject}",
                f"Expéditeur : {contact.email}\n\nMessage :\n {contact.message}",
                contact.email,
                ['aliou@gabithex.fr'],  # mail auquel faut envoyer le message
                fail_silently=False,
            )

            messages.success(request, "Votre message a bien été envoyé. Merci !")
            return render(request, "nene/contact.html", {"form": ContactForm()})  # Réinitialiser le formulaire

        else:
            messages.error(request, "Une erreur est survenue. Vérifiez votre saisie.")
    
    else:
        form = ContactForm()

    return render(request, "nene/contact.html", {"form": form})






#==============================================================
#        PORTFOLIO
#==============================================


def portfolio(request, slug):
    # Récupérer l'employé en fonction du slug
    employee = get_object_or_404(Employee, slug=slug)

    # Récupérer ses expériences, formations et projets
    educations = Education.objects.filter(employee=employee).order_by('-start_date')
    experiences = Experience.objects.filter(employee=employee).order_by('-start_date')
    projects = Project.objects.filter(employee=employee)

    # Récupérer les soft skills
    soft_skills = employee.softSkills.all()

    # Récupérer toutes les technologies associées aux projets et expériences
    tech_from_projects = Technology.objects.filter(projects__employee=employee)
    tech_from_experiences = Technology.objects.filter(experiences__employee=employee)

    # Fusionner les technos sans doublons (via Python)
    technical_skills = set(tech_from_projects) | set(tech_from_experiences)
    
    # recuperer les certifications
    certifications = Certification.objects.filter(employee=employee)


    context = {
        "employee": employee,
        "educations": educations,
        "experiences": experiences,
        "projects": projects,
        "soft_skills": soft_skills,
        "technical_skills": technical_skills,
        "timestamp": now().timestamp(),
        "certifications": certifications
    }

    return render(request, 'nene/portfolio.html', context)



#==============================================================
#             Projet detail
#==============================================
from .models import Project

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'nene/project_detail.html', {'project': project})










#==============================================================
#             
#==============================================

def pricing(request):
    return render(request, 'nene/pricing.html', {"timestamp": now().timestamp()})

def service_details(request):
    return render(request, 'nene/service-details.html', {"timestamp": now().timestamp()})

def services(request):
    return render(request, 'nene/services.html', {"timestamp": now().timestamp()})

def starter_page(request):
    return render(request, 'nene/starter-page.html', {"timestamp": now().timestamp()})

def team(request):
    return render(request, 'nene/team.html', {"timestamp": now().timestamp()})

def testimonials(request):
    return render(request, 'nene/testimonials.html', {"timestamp": now().timestamp()})
