from django.shortcuts import render


def base(request):
    return render(request, 'basic_app/base.html')


def index(request):
    return render(request, 'basic_app/index.html')


def other(request):
    return render(request, 'basic_app/other.html')


def relative(request):
    return render(request, 'basic_app/Relative.html')
