"""cs160_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import url
from django.contrib import admin
#from django.urls import path
from . import views
from django.core.urlresolvers import reverse
from cs160_final.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlspatterns()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url('chapterOne', views.chapterOne, name='chapterOne'),
    url('chapterOneRight', views.chapterOneRight, name='chapterOneRight'),
    url('chapterOneWrong', views.chapterOneWrong, name='chapterOneWrong'),
    url('chapterTwo', views.chapterTwo, name='chapterTwo'),
]
