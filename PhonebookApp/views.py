from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q

from PhonebookApp.forms import PersonForm, PhoneForm, EmailForm
from PhonebookApp.models import Person, Phone, Email


def home(request):
    persons_id = Person.objects.order_by('surname')
    return render(request, 'base.html', {'persons_id': persons_id})


def detail(request, person_id):
    persons_details = Person.objects.get(pk=person_id)
    pemail = Email.objects.filter(person_id=person_id).first()
    persons_phone = Phone.objects.filter(person_id=person_id).first()
    return render(request, 'detail.html', {'persons_details': persons_details, 'pemail': pemail,
                                           'persons_phone': persons_phone})


def add(request):
    if request.method == "POST":
        person_form = PersonForm(request.POST, instance=Person())
        phone_form = PhoneForm(request.POST, instance=Phone())
        email_form = EmailForm(request.POST, instance=Email())
        if person_form.is_valid() or phone_form.is_valid() or email_form.is_valid():
            new_person = person_form.save()
            new_phone = phone_form.save(commit=False)
            new_email = email_form.save(commit=False)
            new_phone.person = new_person
            new_phone.save()
            new_email.person = new_person
            new_email.save()
            return redirect('contact-list')
    else:
        person_form = PersonForm()
        phone_form = PhoneForm()
        email_form = EmailForm()
    return render(request, 'add.html', {
        'person_form': person_form,
        'phone_form': phone_form,
        'email_form': email_form
    })


def contact_list(request):
    contacts = Person.objects.order_by('surname')
    return render(request, 'contact_list.html', {'contacts': contacts})


def delete(request, person_id):
    person = Person.objects.get(pk=person_id)
    phone = Phone.objects.filter(person_id=person_id)
    email = Email.objects.filter(person_id=person_id)
    if request.method == 'POST':
        if phone.exists() or email.exists():
            messages.WARNING(request, "You can't delete this person.")
        else:
            person.delete(), phone.delete(), email.delete()
            return redirect('/phonebookapp/')
    return render(request, 'delete.html', {'person': person,
                                           'phone': phone,
                                           'email': email})


def edit(request, person_id):
    person = Person.objects.get(pk=person_id)
    phone = Phone.objects.filter(person_id=person_id).first()
    email = Email.objects.filter(person_id=person_id).first()
    if request.method == 'POST':
        person_form = PersonForm(request.POST, instance=person)
        phone_form = PhoneForm(request.POST, instance=phone)
        email_form = EmailForm(request.POST, instance=email)
        if person_form.is_valid() or phone_form.is_valid() or email_form.is_valid():
            new_person = person_form.save()
            new_phone = phone_form.save(commit=False)
            new_email = email_form.save(commit=False)
            new_phone.person = new_person
            new_phone.save()
            new_email.person = new_person
            new_email.save()
            return redirect('detail', person_id)
    else:
        person_form = PersonForm(instance=person)
        phone_form = PhoneForm(instance=phone)
        email_form = EmailForm(instance=email)
    return render(request, 'edit.html', {'person_form': person_form,
                                         'phone_form': phone_form,
                                         'email_form': email_form})


def search(request):
    template = "search_results.html"
    query = request.GET.get('q')
    results = Person.objects.filter(Q(name__icontains=query) or Q(surname__icontains=query))
    pages = request, results
    context = {
        'items': pages[0],
        'page_range': pages[1]
    }
    return render(request, template, context)