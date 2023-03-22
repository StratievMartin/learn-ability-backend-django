from rest_framework import serializers
from .models import Course
from .models import Lecture


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "description",
            "price",
            "lectures",
            # "lecturer",
            # "students",
            # "keywords",
            # "comments",
            "created_at",
        ]

        depth = 1


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ["id", "course_id", "title", "description", "video_url", "created_at"]
