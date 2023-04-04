from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # lecturer
    # students
    keywords = models.ManyToManyField("Keyword", related_name="courses")
    # comments
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ", " + self.description


class Lecture(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    content = models.TextField()
    video_url = models.URLField()
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="lectures"
    )
    # lecturer = models.ForeignKey(Lecturer, on_delete=models.SET_NULL)
    # students = models.ManyToManyField(Student, related_name='lectures')
    # comments
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ", " + self.description


class Keyword(models.Model):
    keyword = models.CharField(max_length=50)

    def __str__(self):
        return self.keyword
