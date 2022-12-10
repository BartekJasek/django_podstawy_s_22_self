from django.shortcuts import render, get_object_or_404

from football.models import Team, Game

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


def games_played(request):
    team_id = 1
    team = get_object_or_404(Team, id=team_id)

    games_home = Game.objects.filter(team_home=team)
    games_away = Game.objects.filter(team_away=team)

    games = games_home | games_away

    return render(
        request,
        'games.html',
        context={
            'games': games
        }
    )