from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
import logging

# Create your views here.
Design_post=[
       {'id':1, 'design_title':'Footprint','design_catagories':'Mobile App Design'},
       {'id':2,'design_title':'Pawsquad','design_catagories':'Mobile App Design'},
       {'id':3,'design_title':'Sony Camera','design_catagories':'Mobile App Design'},
       {'id':4,'design_title':'Gaming Web','design_catagories':'Website Design'},
       {'id':5,'design_title':'Beach & Coastal Escapes','design_catagories':'Website Design'},
       {'id':6,'design_title':'feature','design_catagories':'Website Design'},
    ]


def desktophome(request):
    page_title="portfolio"
    job_title="Undergraduate"#variable interpresion syntex
    experiences_yr="2+"#variable interpresion syntex
    Completes_project="5+"#variable interpresion syntex
    User_Name="Buhary Mohamed Asfaq"#variable interpresion syntex
    return render (request,'desktophome.html',
                   {'job_title':job_title,'experiences_yr':experiences_yr,'Completes_project':Completes_project,'User_Name':User_Name,"page_title":page_title,})#variable interpresion syntex
    
def portfolio(request):
    return render (request,'portfolio.html',{"Design_post":Design_post})

def about(request):
    return render (request,'about.html',{})

def contact(request):
    return render (request,'contact.html',{})

def design_details(request, Design_post_id):
    post= next((item for item in Design_post if item['id']== int(Design_post_id)),None)
    logger=logging.getLogger("TESTING")
    logger.debug(f'post variable is {post}')
    return render(request,'portfolio_details.html',{'post':post})

def old_url_redirect(request):
    return redirect(reverse('New_design_details'))

def new_url_view(request):
    return HttpResponse("This is the new Design URL")

