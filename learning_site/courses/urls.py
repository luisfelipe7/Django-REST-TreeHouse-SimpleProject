from django.conf.urls import url
from . import views

urlpatterns = [
    # *************** API VIEWS ************************************
    url(r'^$', views.ListCreateCourse.as_view(), name='coursesList'),
    url(r'(?P<course_pk>\d+)/reviews/$', views.ListCreateReview.as_view(),
        name='reviewsList'),
    url(r'(?P<course_pk>\d+)/reviews/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyReview.as_view(),
        name='reviews_detail'),
    url(r'(?P<pk>\d+)/$', views.RetrieveUpdateDestroyCourse.as_view(),
        name='course_detail'),
    # **************************************************************
]
