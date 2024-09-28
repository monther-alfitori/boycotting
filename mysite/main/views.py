from django.shortcuts import render
from .models import *


def home(request):
    articles = Article.objects.all()
    phrases = Phrase.objects.all().order_by('?')
    brands = Brand.objects.all().order_by('?')
    shares = Share.objects.all()
    companies = Company.objects.all().order_by('?')
    questions = Question.objects.all()


    context = {
        'articles': articles, 
        'phrases': phrases, 
        'brands': brands, 
        'shares': shares, 
        'companies': companies,
        'questions': questions,
    }
    return render(request, 'home.html', context)



def articles(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles.html', context)


def phrases(request):
    phrases = Phrase.objects.all()
    context = {
        'phrases': phrases,
    }
    return render(request, 'phrases.html', context)

def shares(request):
    shares = Share.objects.all()
    context = {
        'shares': shares,
    }
    return render(request, 'shares.html', context)


def boycotting(request):
    boycotting = Company.objects.filter(kind="Boycotted")
    context = {
        'boycotting': boycotting,
    }
    return render(request, 'boycotting.html', context)


def alternatives(request):
    alternatives = Company.objects.filter(kind="Alternative")
    context = {
        'alternatives': alternatives,
    }
    return render(request, 'alternatives.html', context)

    
def boycotters(request):
    boycotters = Brand.objects.all().order_by('?')
    context = {
        'boycotters': boycotters,
    }
    return render(request, 'boycotters.html', context)


def boycotter(request, pk):
    boycotter = Brand.objects.get(id=pk)
    context = {
        'boycotter': boycotter,
    }
    return render(request, 'boycotter.html', context)

    