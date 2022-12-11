from django.shortcuts import render, HttpResponse

from django import views

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


def hello(request):
    return HttpResponse("Hello, world!")


class HelloView(views.View):
    def get(self, request):
        return HttpResponse("Hello, world!")


def hi(request):
    if request.method == "GET":
        return render(
            request,
            'form.html'
        )
    elif request.method == "POST":
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')

        return render(
            request,
            'hi.html',
            context={
                'first_name': first_name,
                'last_name': last_name
            }
        )


# Widoki klasowe - zad 1
class HiView(views.View):
    def get(self, request):
        return render(
            request,
            'form.html'
        )

    def post(self, request):
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')

        return render(
            request,
            'hi.html',
            context={
                'first_name': first_name,
                'last_name': last_name
            }
        )


# Widoki klasowe - zad 2
class ConvertView(views.View):
    def get(self, request):
        return render(
            request,
            'convert.html',
        )

    def post(self, request):
        degrees = int(request.POST.get('degrees'))
        conversion_type = request.POST.get('convertionType')

        if conversion_type == 'celcToFahr':
            result = degrees * 9/5 + 32
            return HttpResponse(f"Wynik: {result} F")

        elif conversion_type == 'FahrToCelc':
            result = (degrees - 32) * 5/9
            return HttpResponse(f"Wynik: {result} C")
