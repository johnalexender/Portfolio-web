from store import views as storeviews
from django.contrib import admin
from django.urls import path, include#step 2 we add the url part just import the "include" keyword after that add pattern here
from . import settings
from django.conf.urls.static import static#update the urls.py import the satic files
from django.contrib.staticfiles.urls import staticfiles_urlpatterns#stataic file in app
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static


handler404 = 'my_portfolio.views.custom_page_not_found'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
    path('', include('pwa.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)