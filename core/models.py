from django.db import models


class Link(models.Model):
    title = models.CharField(name='title', max_length=255,
                             blank=False, null=False)
    link = models.CharField(name='link', max_length=255,
                            blank=False, null=False)
    image = models.ImageField(name='image', upload_to='images')
    category = models.CharField(
        name='category', null=True, blank=True, max_length=255)
    description = models.TextField(
        name='description', blank=True, null=True, max_length=500)
    isLinkOnline = models.BooleanField(
        name='isLinkOnline', blank=True, null=True, default=True)

    def __str__(self):
        return self.title


class Document(models.Model):
    title = models.CharField(
        name='title', max_length=255, null=False, blank=False)
    link = models.CharField(name='link', max_length=255,
                            null=False, blank=False)
    image = models.ImageField(name='image', upload_to='images')
    category = models.CharField(
        name='category', null=True, blank=True, max_length=255)
    description = models.TextField(
        name='description', blank=True, null=True, max_length=500)
    isLinkVerified = models.BooleanField(
        name='isLinkVerified', blank=True, null=True, default=True)

    def __str__(self):
        return self.title
