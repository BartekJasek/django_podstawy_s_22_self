from markupsafe import escape

from django.shortcuts import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello(request):
    return HttpResponse("Hello, world!")


def hello2(request):
    res = """
    <!DOCTYPE html>
    <html>
        <head>
        </head>
        <body>
            <h3>Hello, world!</h3>
        </body>
    </html>
    """
    return HttpResponse(res)


def hi(request):
    return render(request, 'hi.html')


def adam(request):
    return HttpResponse("Witaj, Adam!")


def ewa(reqeust):
    return HttpResponse("Witaj, Ewa!")


def hello_name(request, name):
    safe_name = escape(name)
    return HttpResponse(f"Hello, {safe_name}!")


def hi_name(request, name):
    return render(
        request,
        'name.html',
        context={'name': name}
    )
