from django.db import models

class Project_blog(models.Model):
    title = models.CharField(max_length= 200)
    time = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title
