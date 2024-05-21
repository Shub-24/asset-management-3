from django.db import models
# Create your models here.

class Device(models.Model):

    type = models.CharField(max_length=200, blank=False)
    price = models.IntegerField()

    choices = (
         ('SOLD', 'Item already purchased'),
         ('AVAILABLE', 'Item ready to be purchased'),
         ('RESTOCKING', 'Item restocking in few days')
     )

    status = models.CharField(max_length=10, choices=choices, default="SOLD") # Available, Sold, Restocking
    room = models.CharField(max_length=50, default="Storage Room")


    class Meta:
        abstract = True


    def __str__(self):
        return 'Type: {0} Price: {1}'.format(self.type, self.price)


class Laptop(Device):
    pass

class Desktop(Device):
    pass

class Mobile(Device):
    pass