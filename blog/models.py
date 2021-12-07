from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

App_NameChoices = (
    ('ACE', 'ACE'), ('PBA', 'PBA'), ('TDA', 'TDA'), ('Marketplace', 'Marketplace'), ('IAP', 'IAP'), ('Service Catalogue','Service Catalogue')
)


NotiTriggerForChoices = (('SSL certificate Expiry','SSL certificate Expiry'), ('Password expiry','Password expiry'), ('Client_secrets','Client_secrets'), ('License_expiry','License_expiry'), ('Access to roles expiry','Access to roles expiry'))

FreqChoices = (('hrs','hrs'),('days', 'days'),('months','months'),('years', 'years'))

class Query(models.Model):
    approved = models.BooleanField(default = False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    App_Name = models.CharField(max_length=20, choices=App_NameChoices, default = 'ACE')
    NotiTrigger = models.CharField(max_length=40, choices=NotiTriggerForChoices, default = 'SSL certificate Expiry')
    date_posted = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(default=timezone.now)
    expiry = models.DateTimeField(default=timezone.now)
    frequency = models.CharField(max_length=10, choices=FreqChoices, default = 'hrs')
    nos = models.CharField(max_length=2)
