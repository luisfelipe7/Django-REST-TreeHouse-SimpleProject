from django.shortcuts import get_object_or_404
from courses.models import Course, Step  # or .models import Course

# REST FRAMEWORK IMPORTS
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from . import models
from . import serializers

# REST FRAMEWORK VIEW SETS
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
# NECCESARY TO CUSTOMIZE THE VIEWS
from rest_framework import mixins
# NECCESARY TO PERMISSIONS
from rest_framework import permissions



# Create your views here.

# ****************************   API VIEWS V1  *********************************


class ListCreateCourse(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class RetrieveUpdateDestroyCourse(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class ListCreateReview(generics.ListCreateAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    # We have to define the Review based on the Course
    def get_queryset(self):
        return self.queryset.filter(course__id=self.kwargs.get('course_pk'))

    # We override this method, because this the method that's run right when an object is being created by the View
    def perform_create(self, serializer):
        course = get_object_or_404(
            models.Course, pk=self.kwargs.get('course_pk'))
        serializer.save(course=course)


class RetrieveUpdateDestroyReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    # Get Object is very similar to get Query Set, but get Object get a single item
    def get_object(self):
        return get_object_or_404(self.get_queryset(), course_id=self.kwargs.get('course_pk'), pk=self.kwargs.get('pk'))


# *****************************************************************************

# ****************************   API VIEWS V2 *********************************

class CourseViewSet(viewsets.ModelViewSet):
    # Setting custom permissions
    # If I don't have the permissions can see it
    permission_classes = (permissions.DjangoModelPermissions,)

    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

    # This is to see the reviews of this course
    @detail_route(methods=['get'])
    def reviews(self, request, pk=None):
        self.pagination_class.page_size = 1
        reviews = models.Review.objects.filter(course_id=pk)
        page = self.paginate_queryset(reviews)
        if page is not None:
            serializer = serializers.ReviewSerializer(page,many=True)
            return self.get_paginated_response(serializer.data)

        serializer = serializers.ReviewSerializer(
            reviews, many=True)
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer


# Customized View Set 

class ReviewViewSet2(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer





# *****************************************************************************
