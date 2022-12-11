from django.shortcuts import render


# Cookies - zad 1
def set_cookie(request):
    response = render(
        request,
        'set_cookie.html'
    )
    response.set_cookie('User', 'John')

    return response

