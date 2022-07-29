<<<<<<< Updated upstream
from django.shortcuts import render
=======
from django.shortcuts import render, redirect
# import requests
import json
>>>>>>> Stashed changes

def home(request):
    return render(request, 'index.html')