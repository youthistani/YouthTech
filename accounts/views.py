from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, LoginForm


# Create your views here.
def logout_user(request):
    logout(request)
    messages.success(request, "See you again...")
    return redirect('home')



# def login_user(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             # authenticate
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request,username=username, password=password)
#             login(request, user)
#             messages.success(request, "You have succefully login. Welcome..")
#             return redirect('programs')
#         else:
#             messages.success(request, "Pls fill appropriate..")
#             return redirect('login')
#     else:
#         form = LoginForm()
#         return render(request, 'login.html', {'form':form})

# Assuming you have a login form

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authenticate the user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Login the user
                login(request, user)
                # Redirect to a success page
                return redirect('home')
            else:
                # Invalid credentials
                # Add an error message to the form or context
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()

    # Render the login form (for GET or failed POST)
    return render(request, 'login.html', {'form': form})



def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})