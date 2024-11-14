#we create the inside of app folder to url.py file add those are code then see the url acess to our app 
from django.urls import path # step 3 we add each page url path name
from . import views
#from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.desktophome, name='desktophome'),#path 1
    path('portfolio', views.portfolio, name='portfolio'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('design/<str:Design_post_id>/', views.design_details, name='New_design_details'),
    path('new_url_view',views.new_url_view, name='new_page'),
    path('old_url_redirect',views.old_url_redirect, name='old_url'),
]