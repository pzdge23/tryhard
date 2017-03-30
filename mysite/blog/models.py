from django.db import models

# Create your models here.
# Each class in the model is a table in the database
# Each variable of the class is the column in the table

class Post(models.Model):
    title = models.CharField(max_length = 140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
