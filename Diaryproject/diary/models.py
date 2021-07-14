from django.db import models

class Story(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    weather = models.CharField(max_length=50)
    image = models.ImageField(upload_to = "story/", blank=True, null=True)
    content = models.TextField()

    def __str__(self):
        return self.title