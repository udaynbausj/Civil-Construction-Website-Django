from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls import static
from django.conf.urls.static import static
from authenticate.views import (login_view, logout_view)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index',include('home.urls')),
    url(r'^$',include('home.urls')),
    url(r'^about',include('about.urls')),
    url(r'^contact',include('contact.urls')),
    url(r'^gallary',include('gallary.urls')),
    url(r'^login',login_view,name='login'),
    url(r'^logout',logout_view,name='logout'),
    url(r'^afterlogin',include('authenticate.urls')),
    url(r'^credentials',include('authenticate.urls2')),
    url(r'^progress',include('authenticate.urls3')),
    url(r'^liveprogress',include('authenticate.urls4')),
]
"""if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)"""