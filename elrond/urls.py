"""
URL configuration for elrond project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.views.generic.base import RedirectView
from django.conf.urls.i18n import i18n_patterns
from allauth.account.views import SignupView, LoginView 
from articles.views import CustomSignupView, ArticleListView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),  # <--- this handles language switching
    path("__debug__/", include("debug_toolbar.urls")),
    path("__reload__/", include("django_browser_reload.urls")),

    # path("articles/", include("articles.urls")),
    # path("", SignupView.as_view(), name="account_signup"),
    # # path("accounts/signup/", RedirectView.as_view(url="/")),
    # path("accounts/login/", LoginView.as_view(), name="account_login"),  # use allauth's login view
    #  path("accounts/signup/", SignupView.as_view(), name="account_signup"),
    # path("accounts/", include("allauth.urls")),

 ]

# Allauth URLs should be outside i18n_patterns
urlpatterns += [
    path("accounts/", include("allauth.urls")),
    path("accounts/signup/", CustomSignupView.as_view(), name="account_signup"),
]

urlpatterns += i18n_patterns(
    path("articles/", include("articles.urls")),
    # path("", include("articles.urls")),  # Home should be in i18n
    path('', ArticleListView.as_view(), name='home')

)
# urlpatterns += i18n_patterns(
#     path('', include('articles.urls')),
# )
