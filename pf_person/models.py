from django.db import models


class Person(models.Model):
    name = models.CharField(name='name', max_length=255,
                            blank=True, null=True)
    rg = models.CharField(name='rg', max_length=10,
                          blank=True, null=True, unique=True)
    expedition_time = models.CharField(name='expedition_time', max_length=10,
                                       blank=True, null=True)
    expedition_org = models.CharField(name='expedition_org', max_length=10,
                                      blank=True, null=True)
    cpf = models.CharField(name='cpf', max_length=11,
                           blank=True, null=True, unique=True)
    email = models.CharField(name='email', max_length=70,
                             blank=True, null=True)
    cel = models.CharField(name='cel', max_length=17,
                           blank=True, null=True)
    born_date = models.DateField(name='born_date', null=True, blank=True)
    city = models.CharField(name='city', max_length=17,
                            blank=True, null=True)
    cep = models.CharField(name='cep', max_length=17,
                           blank=True, null=True)
    reference = models.CharField(name='reference', max_length=17,
                                 blank=True, null=True)
    street = models.CharField(name='street', max_length=17,
                              blank=True, null=True)
    street_number = models.CharField(name='street_number', max_length=17,
                                     blank=True, null=True)
    mother_name = models.CharField(name='mother_name', max_length=17,
                                   blank=True, null=True)
    dad_name = models.CharField(name='dad_name', max_length=17,
                                blank=True, null=True)
    partiner_name = models.CharField(name='partiner_name', max_length=17,
                                     blank=True, null=True)

    isPj = models.BooleanField(name='isPj', blank=True, null=True)
    hasGovAccount = models.BooleanField(
        name='hasGovAccount', blank=True, null=True)

    def __str__(self):
        return self.name
