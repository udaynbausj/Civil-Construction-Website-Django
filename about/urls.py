from django.conf.urls import url,include
from . import views

urlpatterns=[
    url(r'^',views.about),
    url(r'^about',views.about),
]