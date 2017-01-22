from django.shortcuts import render
from django.http import HttpResponse
from .models import Representative
from django.views import generic

# Create your views here.
def index(request):
    return render(request,'scenario/index.html')

class RepView(generic.ListView):
    def get_queryset(self):
        return Representative.objects.all()

    


