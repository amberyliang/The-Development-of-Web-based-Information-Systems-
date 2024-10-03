"""final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# register,registered_view,delete_registration,
from django.contrib import admin
from django.urls import path,include
from hospital.views import index,inner_page,login,logout,register,registered_view,delete_registration,post,user_registration,appointment,show_r,profile
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

urlpatterns = [
    # path('accounts/',include('registration.backends.default.urls')),
    path('admin/', admin.site.urls),
    path('', index),
    path('index',index),
    # path('registration/',register, name='registration-url'),
    path('registration',register),
    path('registration/registered/', registered_view, name='registered-url'),
    path('registration/registered/delete/<int:registration_id>/<str:superior>/', delete_registration, name='delete-registration'),
    path('inner_page',inner_page),
    path('login',login),
    path('logout',logout),
    path('post',post),
    path('appointment',appointment),
    path('register',user_registration),
    path('show',show_r),
    path('profile',profile),
    url(r'^captcha/',include('captcha.urls')),
    ]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
