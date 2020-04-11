from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return '%s, %s' % (self.name, self.surname)


class Phone(models.Model):
    person = models.ForeignKey(Person, editable=False, on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return '%s, %s' % (self.person, self.phone_number)


class Email(models.Model):
    person = models.ForeignKey(Person, editable=False, on_delete=models.CASCADE, null=True)
    email = models.EmailField(max_length=254, null=True, blank=True)

    def __str__(self):
        return '%s, %s' % (self.person, self.email)
