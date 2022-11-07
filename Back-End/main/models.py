from django.db import models


# Create your models here.
class file(models.Model):
    the_file = models.FileField(
        upload_to='files',
        default=None
    )


class city(models.Model):
    the_city = models.CharField(
        max_length=40
    )


class province(models.Model):
    the_city = models.ForeignKey(
        city,
        on_delete=models.RESTRICT,
        default=None,
        null=True
    )
    the_province = models.CharField(
        max_length=40
    )


class user(models.Model):
    username = models.CharField(
        max_length=30,
        default=None,
        null=True,
        blank=True,
        unique=True
    )


class user_as(models.Model):
    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        default=None
    )
    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        default=None
    )
    phone_number = models.IntegerField(
        null=True,
        blank=True,
        default=None
    )
    CreatDate = models.DateTimeField(
        null=True,
        blank=True,
        default=None
    )
    profile_image = models.ManyToManyField(
        file,
        blank=True,
        default=None,
        related_name='image_profile'
    )
    city = models.ForeignKey(
        city,
        null=True,
        default=None,
        blank=True,
        on_delete=models.RESTRICT
    )
    province = models.ForeignKey(
        province,
        null=True,
        default=None,
        blank=True,
        on_delete=models.RESTRICT
    )
    username = models.OneToOneField(
        user,
        null=True,
        default=None,
        blank=True,
        on_delete=models.RESTRICT
    )
    password = models.CharField(
        max_length=25,
        default=None,
        null=True
    )
    is_admin = models.BooleanField(
        default=False
    )
    is_active = models.BooleanField(
        default=False
    )
