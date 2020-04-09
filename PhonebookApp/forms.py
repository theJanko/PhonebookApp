from django.forms import ModelForm
from PhonebookApp.models import Person, Phone, Email
from django import forms


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'surname']


class PhoneForm(ModelForm):
    class Meta:
        model = Phone
        exclude = ['person']
        fields = ['phone_number']


class EmailForm(ModelForm):
    class Meta:
        model = Email
        exclude = ['person']
        fields = ['email']
