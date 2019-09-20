"""JobPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from testapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/login/', admin.site.urls),
    url(r'^$', views.start),
    url(r'^hydjobs/', views.hydjobs1),
    url(r'^index', views.index1),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^blorejobs/', views.blorejobs1),
    url(r'^punejobs/', views.punejobs),
    url(r'^chennaijobs/', views.chennaijobs),
    url(r'^logout/', views.logout_view),
    url(r'^signup/', views.signup_view1),
    url('accounts/', include('django.contrib.auth.urls')),
]
