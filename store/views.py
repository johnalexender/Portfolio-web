from django.shortcuts import render,redirect
from django.http import HttpResponse,FileResponse,HttpResponseNotFound
from django.urls import reverse
import logging
from .models import ContactForm  # Import your model
import os
from django.conf import settings



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
                   {'job_title':job_title,
                    'experiences_yr':experiences_yr,
                    'Completes_project':Completes_project,
                    'User_Name':User_Name,
                    "page_title":page_title,})#variable interpresion syntex
    
def portfolio(request,category=None):
    if category:
        design_posts = [design for design in Design_post if design['design_catagories']== category]
    else:
        design_posts = Design_post
        
    return render (request,'portfolio.html',{"Design_post":design_posts})

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

def submit_contact_form(request):
    if request.method == 'POST':
        # Retrieve the form data from the POST request and create a ContactForm object
        contact_form = ContactForm(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            service_of_interest=request.POST.get('service_of_interest'),
            timeline=request.POST.get('timeline'),
            project_details=request.POST.get('project_details')
        )
        
        # Save the form data to the database
        contact_form.save()
        
        # Return a response (for example, a success message)
        return HttpResponse("Form submitted successfully!")

    # If the request is not POST, render the form page
    return render(request, 'portfolio/contact.html')

def download_cv(request):
    # Correctly define the file path relative to the static files
    file_path = os.path.join(settings.BASE_DIR, 'static', 'files', 'CV-IT.pdf')

    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='Your_Resume.pdf')
    else:
        return HttpResponseNotFound("The requested document was not found.")


