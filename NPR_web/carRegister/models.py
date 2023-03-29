from django.db import models


class Point(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    x_relative = models.FloatField(default=0.0)
    camera = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return f"({self.x}, {self.y}, {self.camera})"
