from django.shortcuts import render, get_object_or_404, HttpResponse, redirect

from football.models import Team, Game

# Create your views here.
def league_table(request):
    try:
        fav_id = int(request.COOKIES.get('fav_team'))
    except (ValueError, TypeError):
        fav_id = None

    teams = Team.objects.order_by('-points')

    return render(
        request,
        'league_table.html',
        context={
            'teams': teams,
            'fav_id': fav_id
        }
    )


def games_played(request):
    # team_id = 1
    # Przekazywani inf... zad 3
    team_id = int(request.GET.get('id'))

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


# Formularze - zad 3
def add_game(request):
    if request.method == "GET":
        teams = Team.objects.all()

        return render(
            request,
            'add_game.html',
            context={
                'teams': teams
            }
        )

    elif request.method == "POST":
        try:
            team_home_id = int(request.POST.get('team_home'))
            team_home_goals = int(request.POST.get('team_home_goals'))

            team_away_id = int(request.POST.get('team_away'))
            team_away_goals = int(request.POST.get('team_away_goals'))
        except ValueError:
            return HttpResponse("Niepoprawne dane")

        if team_home_id == team_away_id:
            return HttpResponse("Zespoły nie mogą być takie same")

        team_home = get_object_or_404(Team, id=team_home_id)
        team_away = get_object_or_404(Team, id=team_away_id)

        Game.objects.create(
            team_home=team_home,
            team_home_goals=team_home_goals,
            team_away=team_away,
            team_away_goals=team_away_goals
        )

        # Formularze - Zad 4
        if team_home_goals == team_away_goals:
            team_home.points += 1
            team_away.points += 1

            team_home.save()
            team_away.save()
        elif team_home_goals > team_away_goals:
            team_home.points += 3
            team_home.save()
        else:
            team_away.points += 3
            team_away.save()

        return redirect(f"/games/?id={team_home_id}")


def modify_team(request):
    try:
        team_id = int(request.GET.get('id'))
    except (ValueError, TypeError):
        return HttpResponse("Podano niepoprawne dane")

    team = get_object_or_404(Team, id=team_id)

    if request.method == "GET":
        return render(
            request,
            'modify_team.html',
            context={
                'team': team
            }
        )
    elif request.method == "POST":
        name = request.POST.get('name')
        try:
            points = request.POST.get('points')
        except (ValueError, TypeError):
            return HttpResponse("Podano niepoprawne dane")

        team.name = name
        team.points = points
        team.save()

        return redirect("/table/")


def set_as_favourite(request):
    try:
        team_id = int(request.GET.get('id'))
    except (ValueError, TypeError):
        return HttpResponse("Niepoprawny format danych")

    team = get_object_or_404(Team, id=team_id)

    response = render(
        request,
        'set_as_favourite.html',
        context={
            'team': team,
        }
    )
    response.set_cookie('fav_team', team_id)

    return response
