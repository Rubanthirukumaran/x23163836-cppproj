from django.shortcuts import render
from .models import Donor


def donor_list(request):
    donors = Donor.objects.all()
    return render(request, 'fundraising/donor_list.html', {'donors': donors})

def home(request):
    return render(request, 'fundraising/home.html')


# In your Django views (views.py)
from factorial_library import calculate_factorial

def my_view(request):
    # Example usage: Calculate factorial
    result = calculate_factorial(5)  # Calculate factorial of 5

    # Your view logic...

