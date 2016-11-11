from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User,Group
# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=140)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    #uncertain if this is the correct declaration for Group
    organizer = models.ForeignKey(User, on_delete= models.CASCADE)
    #should we cascade user deletion and event deletion?
    event_date = models.DateTimeField('Event Date')
    created_on = models.DateTimeField('Date Created')
    last_edited_date = models.DateTimeField('Last Edited')
    location = models.CharField(max_length=100)

class Message(models.Model):
    text = models.CharField(max_length=500)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    on_event = models.ForeignKey(Event, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    message_number = models.IntegerField(default=0)
    #message_number will help us maintain order of messages in a given Event