# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    user_id = models.IntegerField(null=True, blank=True)
    user_type = models.CharField(max_length=255, null=True, blank=True)
    date_added = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Order(models.Model):

    #__Order_FIELDS__
    order_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    accepted_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    img_id = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    accepted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pathology = models.BooleanField()
    diagnosis = models.TextField(max_length=255, null=True, blank=True)
    comments = models.TextField(max_length=255, null=True, blank=True)

    #__Order_FIELDS__END

    class Meta:
        verbose_name        = _("Order")
        verbose_name_plural = _("Order")


class Patient(models.Model):

    #__Patient_FIELDS__
    patient_id = models.IntegerField(null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)

    #__Patient_FIELDS__END

    class Meta:
        verbose_name        = _("Patient")
        verbose_name_plural = _("Patient")


class User(models.Model):

    #__User_FIELDS__
    user_id = models.IntegerField(null=True, blank=True)
    user_type = models.CharField(max_length=255, null=True, blank=True)
    date_added = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__User_FIELDS__END

    class Meta:
        verbose_name        = _("User")
        verbose_name_plural = _("User")



#__MODELS__END
