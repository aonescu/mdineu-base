from django.db import models

class Story(models.Model):
    header = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    image = models.URLField()
    link_text = models.CharField(max_length=100)
    link_icon = models.CharField(max_length=100)

    def __str__(self):
        return self.header