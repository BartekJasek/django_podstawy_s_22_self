from django.shortcuts import render

from football.models import Team

# Create your views here.
def league_table(request):

    teams = Team.objects.order_by('-points')

    return render(
        request,
        'league_table.html',
        context={
            'teams': teams,
        }
    )
