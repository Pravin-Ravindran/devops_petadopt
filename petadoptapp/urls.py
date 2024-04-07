"""
URL configuration for the application.
"""
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='Home'),
    path('about/',views.about,name='About'),
    path('checkout/',views.checkout,name='Checkout'),
    path('confirmation/',views.confirmation,name='Confirm'),
    path('contactus/',views.contactus,name='Contact'),
    path('modify/',views.modify,name='Modify'),
    path('revokerequest/',views.revokerequest,name='Revoke'),
    path('updatedetails/',views.updatedetails,name='Updatedetails'),
    path('modifieddetails/',views.modifieddetails,name='Modified'),
    ]
# Django to serve media files at the specified MEDIA_URL
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
