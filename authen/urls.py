from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/', views.register),
    url(r'^login/', views.login),
    url(r'^logout/', views.logout),
    # url(r'^dashboard/', views.dashboard),
    url(r'^forgotpassword/', views.forgotpassword),
    url(r'^(?P<p>[\w\-\_]+)/resetpassword/$',views.resetpassword),
]  