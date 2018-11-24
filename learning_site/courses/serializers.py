from rest_framework import serializers
from . import models

# Creating the serializer for the review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        # This define that the email will be only to write and not to show
        extra_kwargs = {
            'email': {'write_only': True}
        }
        fields = (
            'id',
            'course',
            'name',
            'email',
            'comment',
            'rating',
            'created_at'
        )
        model = models.Review


# Creating the serializer for the Course


class CourseSerializer(serializers.ModelSerializer):
    # This set the foreing key that have the review
    # V1
    # reviews = ReviewSerializer(many=True, read_only=True)
    # V2 (The option to obtain the in other end point)
    # reviews = serializers.HyperlinkedRelatedField(
    #    many=True, read_only=True, view_name='apiv2:review-detail') # Create a link to the review
    # V3 (The Fastest Option)
    reviews = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )

    class Meta:
        fields = (
            'id',
            'created_at',
            'title',
            'description',
            'url',
            'reviews',  # This set the foreing key that have the review
        )
        model = models.Course
