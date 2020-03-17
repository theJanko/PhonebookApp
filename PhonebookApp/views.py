from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from PhonebookApp.forms import PersonForm, PhoneForm, EmailForm

from PhonebookApp.models import Person, Phone, Email


def home(request):
    persons_id = Person.objects.order_by('surname')
    return render(request, 'base.html', {'persons_id': persons_id})


def detail(request, person_id):
    persons_details = Person.objects.filter(Person, pk=person_id)
    pemail = Email.objects.filter(Email, pk=person_id)
    return render(request, 'detail.html', {'persons_details': persons_details, 'pemail': pemail})


def contact_list(request):
    contacts = Person.objects.order_by('surname')
    return render(request, 'contact_list.html', {'contacts': contacts})


def phone_number(request, person_id):
    phone = "Its %s phone number"
    return HttpResponse(phone % person_id)


def email(request, person_id):
    pemail = get_object_or_404(Email, pk=person_id)
    return render(request, 'detail.html', {'pemail': pemail})


def add(request):
    if request.method == 'POST':
        person_form = PersonForm(request.POST)
        phone_form = PhoneForm(request.POST)
        email_form = EmailForm(request.POST)
        if person_form.is_valid() and phone_form.is_valid() and email_form.is_valid():
            person_form.save()
            phone_form.save()
            email_form.save()
            return redirect('home')
    else:
        person_form = PersonForm()
        phone_form = PhoneForm()
        email_form = EmailForm()

    return render(request, 'add.html', {
        'person_form': person_form,
        'phone_form': phone_form,
        'email_form': email_form
    })


def delete(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    if request.method == 'POST':
        person.delete()
        return redirect('/phonebookapp/')
    return render(request, 'delete.html', {'person': person})
