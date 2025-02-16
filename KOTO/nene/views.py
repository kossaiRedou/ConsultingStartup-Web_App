from django.shortcuts import render
from django.utils.timezone import now

def index(request):
    return render(request, 'nene/index.html', {"timestamp": now().timestamp()})

def about(request):
    return render(request, 'nene/about.html', {"timestamp": now().timestamp()})

def blog(request):
    return render(request, 'nene/blog.html', {"timestamp": now().timestamp()})

def blog_details(request):
    return render(request, 'nene/blog-details.html', {"timestamp": now().timestamp()})

def contact(request):
    return render(request, 'nene/contact.html', {"timestamp": now().timestamp()})

def portfolio(request):
    return render(request, 'nene/portfolio.html', {"timestamp": now().timestamp()})

def portfolio_details(request):
    return render(request, 'nene/portfolio-details.html', {"timestamp": now().timestamp()})

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
