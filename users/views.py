from django.shortcuts import render
#from .models import MyUsers
from users.forms import NewUserForm

# Create your views here.

def index(request):
    return render(request, 'users/index.html')

def users(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error: Form Invalid')

    return render(request, 'users/users.html', {'form': form})
