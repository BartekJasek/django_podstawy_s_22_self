from django import views
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


class BandCreateView(views.View):
    def get(self, request):
        return render(
            request,
            'create_band.html',
            context={
                'Band': Band,
            }
        )

    def post(self, request):
        name = request.POST.get('name')
        year = request.POST.get('year')
        still_active = request.POST.get('still_active')
        genre = request.POST.get('genre')

        if still_active == "on":
            still_active = True
        else:
            still_active = False

        Band.objects.create(
            name=name,
            year=year,
            still_active=still_active,
            genre=genre
        )

        return render(
            request,
            'message.html',
            context={
                'name': name,
            }
        )