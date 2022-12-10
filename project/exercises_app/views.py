from django.shortcuts import render, get_object_or_404

from exercises_app.models import Article

from exercises_app.models import Band

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


def show_band(request, band_id):
    band = get_object_or_404(Band, id=band_id)

    return render(
        request,
        'show_band.html',
        context={
            'band': band
        }
    )
