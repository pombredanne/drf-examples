from django.db import models


class Attribute(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey('auth.User')

    def __str__(self):
        return self.name


class Invoice(models.Model):
    name = models.CharField(max_length=128)
    attr = models.ForeignKey(Attribute)

    def __str__(self):
        return self.name
