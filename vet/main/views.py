from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from django.contrib import messages
#from django.http import HttpResponse

# Create your views here.
def home(request):

    # dynamic content
    context = {"clinic_name": "Happy Paws 🐾",
               "tagline": "Your fiendly vet",
               "services": ["Check-ups","X rays", "Dentistry","Vaccinations"]
               }

    return render(request, "home.html", context)

def about(request):
    return render(request, "about.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")


    form = UserCreationForm()
    return render(request, "register.html", {"form": form})

@login_required
def dashboard(request):
    context = {"booking_count": request.user.booking_set.count()}
    return render(request, "dashboard.html", context)

def calculator(request):
    return render(request, "calculator.html")

@login_required
def book(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.owner = request.user
            booking.save()
            messages.success(request, f'Booked{booking.pet_name} in for {booking.date}')
            return redirect("dashboard")
        else:
            messages.error(request, "somthing went wrong")
            return redirect("book")
    else:
        form = BookingForm()
        context = {"form": form}

        return render(request, "book.html", context )