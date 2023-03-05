from .models import Course
from .serializers import CourseSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# from .permissions import IsAdminOrReadOnly


@api_view(["GET", "POST"])
def course_list(request, format=None):
    # get all courses
    # serialize them
    # return json
    if request.method == "GET":
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        # permission_classes = [IsAdminOrReadOnly]
        return Response(serializer.data)

        # JSON
        # serializer = CourseSerializer(courses, many=True)
        # return JsonResponse({"courses": serializer.data})

    if request.method == "POST":
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def course_detail(request, id, format=None):

    try:
        course = Course.objects.get(pk=id)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = CourseSerializer(course, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data)

    elif request.method == "DELETE":
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
