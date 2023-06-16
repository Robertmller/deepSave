from django.db import models


class Link(models.Model):
    title = models.CharField(name='title', max_length=255,
                             blank=False, null=False)
    name = models.CharField(name='name', max_length=255,
                            blank=False, null=False)
