from django.shortcuts import render
from .forms import *
from django.contrib.auth import authenticate, login



# Create your views here.
def register(request):
    form = CustomUserCreatinForm()
    if request.method == 'POST':
        form = CustomUserCreatinForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

    return render(request, 'registration/registration.html', {'form':form})        

