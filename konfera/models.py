from django.db import models


# Create your models here.
class Room(models.Model):
    title = models.CharField(max_length=128)
    
    def __str__(self):
        return self.title


class Location(models.Model):

    title = models.CharField(max_length=128)
    street = models.CharField(max_length=128)
    street2 = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    postcode = models.CharField(max_length=12)
    state = models.CharField(max_length=128)
    capacity = models.IntegerField()

    def __str__(self):
        return "Location: {} {} {} {} {} {} {}".format(
            self.title, self.street, self.street2, self.city,
            self.postcode, self.state, self.capacity)


EVENT_TYPE_CHOICES = (
    ('conference', 'Conference'),
    ('meetup', 'Meetup'),
)

EVENT_STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    ('expired', 'Expired'),
)

class Event(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    event_type = models.CharField(choices=EVENT_TYPE_CHOICES, max_length=20)
    status = models.CharField(choices=EVENT_STATUS_CHOICES, max_length=20)
    location = models.ForeignKey('Location')


class Receipt(models.Model):

    title = models.CharField(max_length=128)
    street = models.CharField(max_length=128)
    street2 = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    postcode = models.CharField(max_length=12)
    state = models.CharField(max_length=128)
    companyid = models.CharField(max_length=32)
    taxid = models.CharField(max_length=32)
    vatid = models.CharField(max_length=32)
    amount = models.FloatField()

    def __str__(self):
        return self.title

