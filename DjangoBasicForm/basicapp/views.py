from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request, 'basicapp/index.html')

def form_name_view(request):
    # if the method is get this form object will be returned.
    form = forms.MyForm()

    # if the method is post this form object will get the value.
    if request.method == 'POST':
        form = forms.MyForm(request.POST)

        if form.is_valid():
            print('Validation success!')
            print('Name: ' + form.cleaned_data['name'])
            print('Email: ' + form.cleaned_data['email'])
            print('Text: ' + form.cleaned_data['text'])

    return render(request, 'basicapp/form_page.html', {'form' : form})
