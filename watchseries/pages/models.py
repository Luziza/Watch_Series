from django.db import models

class Page(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]