from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    context = {}
    return render(request, 'join/login.html', context)


def create_account(request):
    context =  {}
    return render(request, 'join/create-account.html', context)
