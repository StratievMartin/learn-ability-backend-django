"""courses URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from courses import views
from rest_framework.urlpatterns import format_suffix_patterns

# create a route that:
# [] will get all courses depending on the keyword or multiple ones
# [] pushes keywords to the courses arr
# route auth
urlpatterns = [
    path("admin", admin.site.urls),
    # courses
    path("courses", views.course_list),
    path("courses/<int:id>", views.course_detail),
    # lectures
    path("courses/<int:course_id>/lectures", views.course_lectures),
    path("courses/<int:course_id>/lectures/<int:lecture_id>", views.lecture_detail),
    # keywords
    path("keywords", views.keyword_list),
    path("keywords/del/<int:id>", views.keyword_delete),
    path("keywords/<int:id>", views.keyword_delete),
    # pushes keywords to the courses arr
    path("courses/<int:course_id>/keyword/<int:keyword_id>", views.attach_keywords),
    path("courses/search/", views.get_courses_by_keyword),
]

urlpatterns = format_suffix_patterns(urlpatterns)
