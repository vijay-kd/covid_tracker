from django.shortcuts import render
from covid_india import states

# Create your views here.

def home(request):
    return render(
        request,
        "covid_tracker.html",
        {
            'title': 'India Tracker',
            'country' : 'India',
            'data' : states.getdata()
        }
    )