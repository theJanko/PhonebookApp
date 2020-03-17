from django.forms import ModelForm
from PhonebookApp.models import Person, Phone, Email


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'surname']


class PhoneForm(ModelForm):
    class Meta:
        model = Phone
        fields = ['phone_number']


class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = ['email']
