from django.shortcuts import render
from .models import MyUsers

# Create your views here.
def users(request):
    usersData = MyUsers.objects.all()
    users_info_dict = {'usersData' : usersData}
    return render(request, 'users/users.html', users_info_dict)
