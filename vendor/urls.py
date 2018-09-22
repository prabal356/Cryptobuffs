from django.conf.urls import url
from . import views
from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from .models import vendor, RFT, RFP




urlpatterns = [
    #url(r'^$', views.login, name = "login"),
    url(r'^home/$', views.index, name = "index"),
    url(r'^(?P<vendor_id>[0-9]+)/$', views.detail ,name = "detail"),
    url(r'^vendor_homepage/', views.vendor_homepage ,name = "vendor_homepage"),
    url(r'^vendor/(?P<vendor_id_1>[0-9]+)/$', views.vendor_details, name = "vendor_details"),
    url(r'^login/', auth_views.LoginView.as_view(template_name='login.html'), name = "login"),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('', views.index, name='home'),
    url(r'^create_rfp/$', views.create_rfp, name = "RFP"),
    url(r'^create_rft/$', views.create_rft, name = "RFT"),
    url(r'^rft(?P<rft_id>[0-9]+)/$', views.rft_details, name = "rft_details")
    #url(r'^/vendor/rft(?P<vendor_id>[0-9]+)/$', views.r)
]

