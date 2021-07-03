
from django.contrib import admin
from django.urls import path,include
from home import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
   path("", views.index,  name='home'),
   path("About", views.about, name='about'),
   path("Contact", views.contact, name='contact'),
]
# if settings.DEBUG:
#       urlpatterns += static(settings.MEDIA_URL,
#       document_root=settings.MEDIA_ROOT)