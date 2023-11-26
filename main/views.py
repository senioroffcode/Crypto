from django.shortcuts import render
from .models import *

def index_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        message = request.POST.get("message")
        contact = Contact.objects.create(
            username=username,
            email=email,
            message=message,
        )
    context = {
        'crypto': Crypto.objects.all(),
        'will': Will.objects.all(),
        'token':Token.objects.all(),
        'btc': Btc.objects.all(),
        'clock': Clock.objects.all(),
        'partner': Partner.objects.all(),
        'business': Business.objects.all(),
        'paper': Paper.objects.all(),
        'team': Team.objects.all(),
        'contact' : Contact.objects.all(),
    }
    return render(request, 'index.html', context)

def index_two_view(request):
    context = {
        "world":World.objects.all(),
        "icon": Icon.objects.all(),
        "about": About.objects.all(),
        "choose": Choose.objects.all(),
        "active": Active.objects.all(),
        "trey": Trey.objects.all(),
        "team": Team.objects.all(),
        'frequent': Frequent.objects.all(),

    }
    return render(request, 'index-2.html', context)


def blog_view(request):
    context = {
      "article":Article.objects.all()
    }
    return render(request, 'blog.html', context)


def blog_details_view(request):
    context = {
      "article":Article.objects.all(),
      "app":App.objects.all()
    }
    return render(request, 'blog-details.html', context)