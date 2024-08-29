from django.shortcuts import render


# Create your views here.
def home(requests):
    return render(requests, "home.html")


def contacts(requests):
    return render(requests, "contacts.html")