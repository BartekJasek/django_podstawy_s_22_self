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