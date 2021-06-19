from django.db import models

class Lang(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Tech(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Teams(models.Model):
    name = models.CharField(max_length=32)
    work = models.CharField(max_length=32)
    points = models.IntegerField(null=True)
    langs = models.ManyToManyField(Lang)
    techs = models.ManyToManyField(Tech)

    def __repr__(self):
        return "{}: {}".format(self.pk, self.name)

    __str__ = __repr__ 