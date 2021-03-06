
from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import RedirectView


urlpatterns = [
    path("", TemplateView.as_view(template_name='base.html'), name='home'),
    # path("", TemplateView.as_view(template_name='base.html'), name='start'),
    path("services", TemplateView.as_view(template_name='services.html'), name='services'),
    path("about", TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', include('contact.urls')),
    path('admin/', admin.site.urls),

    # path('home', RedirectView.as_view(url=reverse_lazy('job_application:job_application'))),
    path('account/', include('account.urls',)),
    path('assessment/', include('assessment.urls',)),
]







"""gcosfinance URL Configuration

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
