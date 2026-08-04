from django.shortcuts import render


def boas_vindas(request):
    return render(request, 'core/boas_vindas.html')
