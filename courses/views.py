from .models import Course
from .serializers import CourseSerializer
from django.http import JsonResponse


def course_list(request):
    # get all courses
    # serialize them
    # return json

    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return JsonResponse({"courses": serializer.data}, safe=False)
