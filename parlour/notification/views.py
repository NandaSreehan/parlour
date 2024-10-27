from django.shortcuts import render
from notification.models import notif
def note(request):
    return render(request,'notes.html')

# Create your views here.
