from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _
from events_site.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label='Имя', max_length=150, required=True)
    last_name = forms.CharField(label='Фамилия', max_length=150, required=True)
    birthdate = forms.DateField(label='Дата рождения', required=True, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'birthdate')
        field_classes = UserCreationForm.Meta.field_classes
