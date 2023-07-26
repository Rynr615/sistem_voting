# user_registration/views.py
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Ubah ke halaman index setelah signup berhasil
    else:
        form = SignupForm()
    return render(request, 'user\signup.html', {'form': form})

# user_registration/views.py

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Ganti 'index' dengan nama URL untuk halaman index Anda
            else:
                form.add_error(None, 'Invalid credentials. Please try again.')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})


# views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def profile(request):
    return render(request, 'user/profile.html')



