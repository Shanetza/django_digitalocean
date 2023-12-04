from django.db import models

# Create your models here.
class Goal(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title