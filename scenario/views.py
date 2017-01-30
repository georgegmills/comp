from django.shortcuts import render, get_object_or_404,render, render_to_response, redirect 
from django.http import HttpResponse
from .models import Representative, CompPlan
from django.views import generic



# Create your views here.
def index(request):
    return render(request,'scenario/index.html')

def RepView(request,template_name='scenario/representative_list.html'):
          args = {}
          args['representative_list'] = Representative.objects.all()
          dummy_data = [["Jan", 44],["Feb", 44],["Mar", 44]]
          args['data'] = dummy_data 

          return render_to_response(template_name,args)


def PlanView(request,template_name='scenario/plan_list.html'):
          args = {}
          args['plan_list'] = CompPlan.objects.all()
          dummy_data = [["Jan", 44],["Feb", 44],["Mar", 44]]
          args['data'] = dummy_data 

          return render_to_response(template_name,args)

    


