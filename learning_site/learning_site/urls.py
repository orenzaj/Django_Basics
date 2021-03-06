"""learning_site URL Configuration

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

# Look at docs for these
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views     # Import views from current directory

urlpatterns = [
    url(r'^courses/', include('courses.urls', namespace='courses')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.my_first_view, name='Home'),    # This will be the pattern for index
]

# This checks if we're in DEBUG mode,
# Adds /static/ path that points to all our files in our static folder
urlpatterns += staticfiles_urlpatterns()
