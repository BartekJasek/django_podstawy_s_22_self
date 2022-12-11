from django.shortcuts import render, HttpResponse


# Cookies - zad 1
def set_cookie(request):
    response = render(
        request,
        'set_cookie.html'
    )
    response.set_cookie('User', 'John')

    return response


def show_cookie(request):

    user = request.COOKIES.get('User')
    if not user:
        return HttpResponse("Brak użytkownika")

    return render(
        request,
        'show_cookie.html',
        context={
            'user': user,
        }
    )


def delete_cookie(request):
    response = HttpResponse("OK")
    response.delete_cookie('User')

    return response


def add_to_cookie(request):
    if request.method == "GET":
        return render(
            request,
            'add_to_cookie.html'
        )

    elif request.method == "POST":
        key = request.POST.get('key')
        value = request.POST.get('value')

        if not key:
            return HttpResponse("Brak key")

        response = HttpResponse("Zapisano")
        response.set_cookie(key, value)

        return response


def set_session(request):
    request.session['counter'] = 0
    return HttpResponse("Ok")


def show_session(request):
    counter = request.session['counter']
    request.session['counter'] += 1

    return HttpResponse(counter)


def delete_session(request):
    del request.session['counter']

    return HttpResponse("Usunięto klucz counter z sesji.")


def login_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        request.session['loggedUser'] = name

    user = request.session.get('loggedUser')
    if user:
        return render(
            request,
            'hello.html',
            context={
                'user': user
            }
        )

    return render(
        request,
        'login.html'
    )


def add_to_session(request):
    if request.method == "GET":
        return render(
            request,
            'add_to_session.html'
        )

    elif request.method == "POST":
        key = request.POST.get('key')
        value = request.POST.get('value')

        if not key:
            return HttpResponse("Brak key")

        request.session[key] = value
        return HttpResponse("Zapisano")


def show_all_session(request):
    data_session = request.session.items()

    return render(
        request,
        'show_all_session.html',
        context={
            'data_session': data_session
        }
    )