from rest_framework import serializers
from .models import Course
from .models import Lecture


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "title", "description", "price"]

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ["id", "title", "description", "video_url", "course_id", "created_at"]
