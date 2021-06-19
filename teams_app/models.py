from django.db import models

class Teams(models.Model):
    name = models.CharField(max_length=32)
    work = models.CharField(max_length=32)
    points = models.IntegerField(null=True)

    def __repr__(self):
        return "{}: {}".format(self.pk, self.name)

    __str__ = __repr__ 