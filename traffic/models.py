from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class People(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=20, help_text="The Name of the person")
    age = models.IntegerField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

@receiver(post_save, sender=User)
def create_people(sender, instance, created, **kwargs):
    if created:
        People.objects.create(user=instance)
        print("Profile created ")
# post_save.connect(create_people, sender=User)


class Junction(models.Model):
    name = models.CharField(max_length=20, help_text="Name of the Junction Exchange")
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Road(models.Model):
    direction_choice = (
        ('R', 'Right to left'),
        ('L', 'Left to right'),
        ('U', 'Up to down'),
        ('D', 'down to up'),
    )
    road_status = (
        ('A', 'Available'),
        ('M', 'Maintenance'),
        ('R', 'Restricted'),
    )
    name = models.CharField(max_length=20, help_text="The road name", null=True, blank=True)
    distance = models.FloatField(help_text="The distance of the road", null=True, blank=True)
    direction = models.CharField(max_length=2, help_text="The direction of the road",choices=direction_choice)
    traffic_queue = models.IntegerField(null=True, blank=True)
    junction = models.ForeignKey('Junction',null=True, blank=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, blank=True, null=True, help_text="Road status availability", default='A')
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('road-detail', args=[str(self.id)])

class Light(models.Model):
    state_choice = (
        ('on', 'ON'),
        ('off', 'OFF'),
    )

    lights  = (
        ('light1', 'light1'),
        ('light2', 'light2'),
        ('light3', 'light3'),
        ('light4', 'light4'),
        ('light5', 'light5'),
        ('light6', 'light6'),
        ('light7', 'light7'),
        ('Auto', 'Auto'),
    )

    name = models.CharField(max_length=20,choices=lights, help_text="The light on the road")
    state = models.CharField(max_length=3, choices=state_choice)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    road = models.ForeignKey(Road, blank=True, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.name


class Traffic(models.Model):
    traffic_status = (
        ('hp', 'High Populoated'),
        ('lp', 'Low Populoated'),
        ('mp', 'Medium Populoated'),
    )

    time = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    count = models.IntegerField(help_text="The total number of cars on the road")
    road = models.ForeignKey('Road', on_delete=models.CASCADE)
    status = models.CharField(max_length=2, default='mp',)
    image = models.ImageField(upload_to='traffic', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.time} and {self.count}"

    def get_absolute_url(self):
        return reverse('traffic-detail', args=[str(self.id)])

