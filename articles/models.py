from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    content = models.TextField()
    # keywords = models.ManyToManyField("Keyword", related_name="courses")
    # author
    # comments
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ", " + self.description
