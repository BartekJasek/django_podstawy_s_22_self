from django.shortcuts import render, HttpResponse


# Create your views here.
def one(request):

    start = request.GET.get('start')
    end = request.GET.get('end')

    if not start or not end:
        return HttpResponse("Brak wymaganych parametrów ('start', 'end')")


    # opcjonlanie (za pomoca petli)
    # result = []
    # while start < end:
    #     result.append(start)
    #     start = start+1

    result = list(range(int(start), int(end)))

    return render(
        request,
        'one.html',
        context={
            'result': result
        }
    )


def hello(request):
    first_name = request.POST.get('first-name')
    last_name = request.POST.get('last-name')

    if not first_name or not last_name:
        return render(
            request,
            'form.html'
        )
    else:
        return render(
            request,
            'hello.html',
            context={
                'first_name': first_name,
                'last_name': last_name
            }
        )


def convert(request):
    if request.method == "GET":
        return render(
            request,
            'convert.html',
        )

    elif request.method == "POST":
        degrees = int(request.POST.get('degrees'))
        conversion_type = request.POST.get('convertionType')

        if conversion_type == 'celcToFahr':
            result = degrees * 9/5 + 32
            return HttpResponse(f"Wynik: {result} F")

        elif conversion_type == 'FahrToCelc':
            result = (degrees - 32) * 5/9
            return HttpResponse(f"Wynik: {result} C")
