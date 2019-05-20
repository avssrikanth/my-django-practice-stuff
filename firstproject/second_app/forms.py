from django import forms
from second_app.models import MyUser

class Newuserform(forms.ModelForm):
    class Meta():
        model=MyUser
        fields="__all__"