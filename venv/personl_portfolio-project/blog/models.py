from django.db import models

class Article(models.Model):
  title = models.CharField(max_length=300)
  timedate = models.DateTimeField(auto_now=False, auto_now_add=False)
  description = models.TextField()