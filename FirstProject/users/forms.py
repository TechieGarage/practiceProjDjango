from django import forms
from users.models import MyUsers

class NewUserForm(forms.ModelForm):
    class Meta:  # Inline class
        model = MyUsers
        #fields = '__all__'
        # fields = ('fname','myEmail')
        exclude = ('fname',)
