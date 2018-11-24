"""learning_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# This import is necessary for the url
from django.conf.urls import url, include
from django.urls import path
# We need to import for the view, the point means that includes all the views from the file
from . import views
# For the static files, the static is because the debug mode is activated
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from cruds_adminlte.urls import crud_for_app

# ******************* API VERSION 2 ***************************
from rest_framework import routers
from courses.views import CourseViewSet, ReviewViewSet, ReviewViewSet2
from rest_framework.documentation import include_docs_urls


router = routers.SimpleRouter()
router.register(r'courses', CourseViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'reviews2', ReviewViewSet2)


urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$', views.hello_world, name="welcome"),  # http://127.0.0.1:8000/
    # Convert the courses.url in a path
    # Is important to set the version of the url
    url(r'^api/v1/courses/',
        include(('courses.urls', 'courses'), namespace='courses')),

    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^api/v2/courses/', include((router.urls, 'courses'), namespace='apiv2')),
    url(r'^docs/', include_docs_urls(title='Learning API', public=True)),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += crud_for_app('courses')
