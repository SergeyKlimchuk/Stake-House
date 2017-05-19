from django.shortcuts import render


def about(request):
    return render(request, 'main/about.html')


def beer(request):
    return render(request, 'main/beer.html')


def contact(request):
    return render(request, 'main/contact.html')


def food(request):
    return render(request, 'main/food.html')


def index(request):
    return render(request, 'main/index.html')


def reservation(request):
    return render(request, 'main/reservation.html')

def index2(request):
    return render(request, 'main/index2.html')
