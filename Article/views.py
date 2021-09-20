from django.shortcuts import render


def Product(request):
    return render(request, 'Shop.html')
