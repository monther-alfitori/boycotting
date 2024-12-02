from django.shortcuts import render
from .models import *
from django.db.models import Q
import random


def home(request):
    articles = Article.objects.all()
    phrases = Phrase.objects.all().order_by('?')
    brands = Brand.objects.all().order_by('?')
    shares = Share.objects.all().order_by('?')
    products = Product.objects.all().order_by('?')
    questions = Question.objects.all()


    context = {
        'articles': articles, 
        'phrases': phrases, 
        'brands': brands, 
        'shares': shares, 
        'products': products,
        'questions': questions,
    }
    return render(request, 'home.html', context)



def articles(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles.html', context)


def article(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        'article': article,
    }
    return render(request, 'article.html', context)


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
    boycotting = Product.objects.filter(kind="Boycotted")
    context = {
        'boycotting': boycotting,
    }
    return render(request, 'boycotting.html', context)


def alternatives(request):
    alternatives = Product.objects.filter(kind="Alternative")
    context = {
        'alternatives': alternatives,
    }
    return render(request, 'alternatives.html', context)


def product(request, pk):
    product = Product.objects.get(id=pk)
    # Fetch products of the same kind and exclude the current product
    related_products = Product.objects.filter(kind=product.kind).exclude(id=product.id)
    # Randomly select up to 8 products
    related_products = random.sample(list(related_products), min(10, related_products.count()))
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'product.html', context)

    
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

    