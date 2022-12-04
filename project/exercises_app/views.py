from django.shortcuts import render

from exercises_app.models import Article


# Create your views here.
def articles(request):

    article_list = Article.objects.all()  # filter(status=2)

    return render(
        request,
        'articles.html',
        context={
            'article_list': article_list
        }
    )
