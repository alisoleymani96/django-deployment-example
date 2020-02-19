from django.shortcuts import render
from django.http import HttpResponse
from .models import AccessRecord


def index(request):
    context = {}
    acc_recs = AccessRecord.objects.order_by('date')
    context['AccessRecords'] = acc_recs
    return render(request, 'first_app/index.html', context=context)
