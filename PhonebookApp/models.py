from django.db import models


class Person(models.Model):
    name = models.CharField('Name', max_length=50)
    surname = models.CharField('Surname', max_length=50)

    def __str__(self):
        return '%s, %s' % (self.name, self.surname)


class Phone(models.Model):
    person = models.ForeignKey(Person, editable=False, on_delete=models.CASCADE)
    phone_number = models.CharField('Phone number', max_length=50)

    def __str__(self):
        return '%s, %s' % (self.person, self.phone_number)


class Email(models.Model):
    person = models.ForeignKey(Person, editable=False, on_delete=models.CASCADE)
    email = models.EmailField('Email', max_length=254)

    def __str__(self):
        return '%s, %s' % (self.person, self.email)
