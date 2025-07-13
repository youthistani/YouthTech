from django.shortcuts import render, redirect
from .models import Donor
from .forms import DonorRegistrationForm
from django.contrib import messages
# Create your views here.
def index(request):
    """
    this fnc will provide the donation list to frontend.
    
    """
    donations = Donor.objects.all()
    return render(request, 'donation_list.html', {'donors': donations})

def register_donor(request):
    if request.method == 'POST':
        form = DonorRegistrationForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            try:
                age = int(request.POST["age"])
            except Exception as e:
                messages.success(request, "e")
                return redirect('register_donor')
            
            
            if age > 40:
                # print("hello, I am in the loop")
                messages.success(request, "Sorry, You are age is Over the criterea.")
                return redirect('register_donor')
            elif age < 20:
                # print("hello, I am in the loop")
                messages.success(request, "Sorry, You are age is Under the criterea.")
                return redirect('register_donor')
            else:
                form.save()
                return redirect('donation_list')
        else:
            messages.success(request, "Please Fill appropriate.")
            return redirect('register_donor')
    else:
        form = DonorRegistrationForm()
    return render(request, 'register_donor.html', {'form': form})