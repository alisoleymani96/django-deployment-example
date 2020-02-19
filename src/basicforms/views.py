from django.shortcuts import render
from . import forms


def index(request):
    return render(request, 'basicforms_app/index.html', context={})


def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("the name is " + form.cleaned_data['Name'])

    return render(request, 'basicforms_app/form_page.html', {'form': form})
