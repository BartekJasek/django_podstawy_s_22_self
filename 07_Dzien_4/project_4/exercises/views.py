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
