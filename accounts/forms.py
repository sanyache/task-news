from allauth.account.forms import SignupForm
from django import forms
from .models import MyUser
from django.contrib.auth.models import User


class DateInput(forms.Form):
    input_type = 'date'


class CustomSignupForm(SignupForm):
    """
    Extended SignupForm for MyUser model
    """
    birth_day = forms.DateField(label='Birthday')
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    class Meta:
        widgets = {'birth_day': DateInput()}


    def custom_signup(self, request, user):
        super(CustomSignupForm, self).custom_signup(request, user)
        birth_day = self.cleaned_data.get('birth_day')
        profile = MyUser.objects.create(user=user, birth_day=birth_day)



