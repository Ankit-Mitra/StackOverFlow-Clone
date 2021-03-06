"""HomeSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from Contact import views
from django.conf.urls.static import static

admin.sites.AdminSite.site_header = 'StackOverFlow Clone Administration'
admin.sites.AdminSite.site_title = 'StackOverFlow Clone Administration'
admin.sites.AdminSite.index_title = 'Ankit Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('Landingpage/',views.landing,name='landing'),
     path('Contact/',views.contact,name='contact'),

     #Authentication,Should I make set of url in Authentication app?
    path('Signup/',views.signupuser,name='register'),
    path('login/',views.loginuser,name='login'),
    
]


handler404 = 'Contact.views.error_404_view'  #myapp.views.viewname

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)









