from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    page_count = models.PositiveIntegerField()
    publish_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
