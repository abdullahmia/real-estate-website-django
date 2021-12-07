from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
import time

from contact.models import Contact

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        # get values
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Your are now loged in')
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')



def user_signup(request):
    if request.method == 'POST':
        # Get data from values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # if password match
        if password == password2:
            # username exist
            if User.objects.filter(username=username).exists():
                messages.add_message(request, messages.ERROR, 'This username is already taken')
                return redirect('signup')
            else:
                if User.objects.filter(email=email).exists():
                    messages.add_message(request, messages.ERROR, 'The email is being used')
                else:

                    # all is good
                    user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                    # login after Signup
                    # auth.login(request, user)
                    # messages.add_message(request, messages.SUCCESS, 'Your account has been successfully creat')
                    # return redirect('dashboard')
                    user.save()
                    messages.add_message(request, messages.SUCCESS, 'Account created...!')
                    return redirect('login')

        else:
            messages.add_message(request, messages.ERROR, 'Password do not match')
            return redirect('signup')
    return render(request, 'accounts/signup.html')

def user_logout(request):
    auth.logout(request)
    messages.add_message(request, messages.WARNING, 'Your Log out')
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):

    currentTime = int(time.strftime('%H'))
    grettings = ''
    if currentTime < 12:
        grettings = 'Good morning'
    if currentTime > 12:
        grettings = 'Good afternoon'
    if currentTime > 6:
        grettings = 'Good evening'
    user_contact = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    ctx = {'user_contact': user_contact, 'grettings': grettings}
    return render(request, 'accounts/dashboard.html', ctx)




@login_required
def user_password_change(request):
    if request.method == "POST":
        fm = PasswordChangeForm(request.user, request.POST)
        if fm.is_valid():
            changed = fm.save()
            update_session_auth_hash(request, changed)
            messages.add_message(request, messages.SUCCESS, "Password Has Been Changed...!")
            return redirect('teacher_dashboard')
    else:
        fm = PasswordChangeForm(request.user)
    return render(request, 'accounts/password_change.html', {'fm': fm})
