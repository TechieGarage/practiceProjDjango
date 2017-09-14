from django import forms
from django.core import validators

# custom validator
#def check_for_z(value):
#    if not value.lower().startswith('z'):
#        raise forms.ValidationError('NAME NEEDS TO START WITH Z')

class MyForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)

    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])

    def clean(self):   # clean entire form
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError('Make sure emails match!')

    #def clean_botcatcher(self):        # clean_<attribute> ---> clean specific attribute
    #    botcatcher = self.cleaned_data['botcatcher']
    #    if len(botcatcher) > 0:
    #        raise forms.ValidationError('GOTCHA BOT!')
    #    return botcatcher
