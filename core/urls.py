"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from bsct.urls import URLGenerator
from user_accounts import models as umodels, views as uviews
from opportunities import models as omodels, views as oviews

user_urls = URLGenerator(umodels.User).get_urlpatterns(crud_types="crud")
acc_urls = URLGenerator(omodels.Account).get_urlpatterns(crud_types="crud")
opp_urls = URLGenerator(omodels.Opportunity).get_urlpatterns(crud_types="crud")


urlpatterns = [
    path("admin/", admin.site.urls),
    url(r"", include(user_urls)),
    url(r"", include(acc_urls)),
    url(r"", include(opp_urls)),
    url(r"^users/", uviews.user_list, name="user_list"),
    url(r"^users/register/", uviews.sign_up, name="register"),
    url(r"^users/login/", uviews.LoginView.as_view(), name="login"),
    url(r"^accounts/", oviews.acc_list, name="account_list"),
    url(r"", oviews.index, name="index"),
    url(r"^opportunities/", oviews.opp_list, name="opportunity_list"),
    url(r"^user/(?P<pk>\d+)/", uviews.user_update, name="user_update"),
    url(r"^user/(?P<pk>\d+)/", uviews.user_delete, name="user_delete"),
]
