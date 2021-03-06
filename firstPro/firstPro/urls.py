
"""firstPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
#from firstPro.views import homepage
from . import views
from django.urls import path
urlpatterns = [
    url('admin/', admin.site.urls),
    #path('',views.IndexHome.as_view(),name='Homepage'),
    url(r'scheduleGen/', include('scheduleGen.urls')),
    #url(r'^$', include('scheduleGen.urls')),
    url(r'classReview/', include('classReview.urls')),
    url(r'', include('Home.urls')),
    #url(r'^$', include('classReview.urls')),
    url(r'account/', include('account.urls')),
    url(r'class/', include('class.urls')),
    url(r'classR/', include('classR.urls')),
    url(r'classT/', include('classT.urls')),
    url(r'classU/', include('classU.urls')),
    url(r'classV/', include('classV.urls')),
    url(r'classW/', include('classW.urls')),
    url(r'majors/', include('majors.urls')),
    url(r'mission/', include('mission.urls')),
    url(r'classes/', include('classes.urls')),
    url(r'csci/', include('csci.urls')),
    url(r'cyber/', include('cyber.urls')),
    url(r'mis/', include('mis.urls')),
    url(r'itinn/', include('itinn.urls')),
    url(r'bioi/',include('bioi.urls')),


]
