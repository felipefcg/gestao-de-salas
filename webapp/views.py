from django.shortcuts import render


def boas_vindas(request):
    return render(request, 'webapp/boas_vindas.html')
