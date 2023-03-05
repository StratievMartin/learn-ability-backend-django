from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    # price
    # lecturer
    # lectures
    # students
    # keywords
    # comments
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ", " + self.description

# class Lectures(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.CharField(max_length=500)
#     # price
#     # lecturer
#     # lectures
#     # students
#     # keywords
#     # comments
#     # created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title + ", " + self.description
