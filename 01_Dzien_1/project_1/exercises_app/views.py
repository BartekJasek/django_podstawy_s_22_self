import random

from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("Hello, world!")


def random_view(request):
    number = random.randint(0, 100)
    return render(
        request,
        'random.html',
        context={'number': number}
    )


def random_view_2(request, max_number):
    number = random.randint(0, max_number)

    return render(
        request,
        'random2.html',
        context={
            'max_number': max_number,
            'number': number,
        }
    )


def random_view_3(request, min_number, max_number):
    number = random.randint(min_number, max_number)

    return render(
        request,
        'random3.html',
        context={
            'min_number': min_number,
            'max_number': max_number,
            'number': number,
        }
    )


def hello_name(request, name):
    return render(
        request,
        'hello.html',
        context={'name': name}
    )
