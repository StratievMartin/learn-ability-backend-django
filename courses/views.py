from .models import Course, Lecture, Keyword
from .serializers import CourseSerializer, LectureSerializer, KeywordSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# from .permissions import IsAdminOrReadOnly


@api_view(["GET", "POST"])
def course_list(request, format=None):
    if request.method == "GET":
        try:
            courses = Course.objects.all()
        except Course.DoesNotExist:
            return Response(
                {"error": "No existing courses"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = CourseSerializer(courses, many=True)
        # permission_classes = [IsAdminOrReadOnly]
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CourseSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def course_detail(request, id, format=None):
    try:
        course = Course.objects.get(pk=id)
    except Course.DoesNotExist:
        return Response(
            {"error": f"Course with id: {id} doesn't exist"},
            status=status.HTTP_404_NOT_FOUND,
        )

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


@api_view(["GET", "POST"])
def course_lectures(request, course_id, format=None):
    try:
        course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        return Response(
            {"error": "Course doesn't exist"}, status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":
        lectures = Lecture.objects.filter(course_id=course_id)
        if not lectures:
            return Response(
                {"error": "No Lectures found for this course"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = LectureSerializer(lectures, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = LectureSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(course=course)
        return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
def lecture_detail(request, course_id, lecture_id, format=None):
    try:
        course = Course.objects.get(pk=course_id)
        lecture = course.lectures.get(pk=lecture_id)
    except Course.DoesNotExist:
        return Response(
            {"error": f"Course with id: {course_id} doesn't exist"},
            status=status.HTTP_404_NOT_FOUND,
        )
    except Lecture.DoesNotExist:
        return Response(
            {
                "error": f"Lecture with id: {lecture_id} doesn't exist in course {course_id}"
            },
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        serializer = LectureSerializer(lecture)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = LectureSerializer(lecture, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(course=course)
        return Response(serializer.data)

    elif request.method == "DELETE":
        lecture.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST", "PUT", "DELETE"])
def keyword_list(request, format=None):
    if request.method == "GET":
        try:
            keywords = Keyword.objects.all()
        except Keyword.DoesNotExist:
            return Response(
                {"error": "No existing keywords"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = KeywordSerializer(keywords, many=True)
        # permission_classes = [IsAdminOrReadOnly]
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = KeywordSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def keyword_detail(request, course_id, keyword_id, format=None):
    print(keyword_id, course_id)
    # try:
    #     course = Course.objects.get(pk=course_id)
    #     keyword = course.lectures.get(id=keyword_id)
    # except Course.DoesNotExist:
    #     return Response(
    #         {"error": f"Course with id: {course_id} doesn't exist"},
    #         status=status.HTTP_404_NOT_FOUND,
    #     )
    # except Keyword.DoesNotExist:
    #     return Response(
    #         {
    #             "error": f"Keyword with id: {keyword_id} doesn't exist in course {course_id}"
    #         },
    #         status=status.HTTP_404_NOT_FOUND,
    #     )

    # if request.method == "GET":
    #     serializer = KeywordSerializer(keyword)
    #     return Response(serializer.data)

    # elif request.method == "PUT":
    #     serializer = KeywordSerializer(keyword, data=request.data)
    #     if not serializer.is_valid():
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     serializer.save(keyword=keyword)
    #     return Response(serializer.data)

    # elif request.method == "DELETE":
    #     keyword.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
