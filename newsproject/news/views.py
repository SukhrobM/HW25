from django.shortcuts import render, redirect
from .models import NewsCategory, News


# Create your views here.
def home_page(request):
    categories = NewsCategory.objects.all()
    articles = News.objects.all()
    context = {
        'categories': categories,
        'articles': articles
    }
    return render(request, 'home.html', context)


def get_articles(request, pk):
    article = News.objects.get(id=pk)
    context = {
        'article': article
    }
    return render(request, 'articles.html', context)


def get_category(request, pk):
    exact_category = NewsCategory.objects.get(id=pk)
    article = News.objects.filter(news_category=exact_category)
    context = {
        'articles': article,
        'category': exact_category
    }
    return render(request, 'categories.html', context)


def search_article(request):
    if request.method == 'POST':
        search_name = request.POST.get('search_article')
        try:
            search_result = News.objects.get(news_headline=search_name)
            return redirect(f'articles/{search_result.id}')
        except:
            print('Не найдено')
            return redirect('/')
