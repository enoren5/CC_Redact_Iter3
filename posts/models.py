from django.db import models
import datetime
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=161)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()
    now = datetime.datetime.now()

    def __str__(self):
        return self.title

    def pub_date_preference(self):
        # a = self.pub_date.timezone.now("US")
        b = self.pub_date.strftime("%A %d %B %Y @ %I:%M:%S %p")
        # c = pytz.timezone("US")
        return (b)

    def summary(self):
        return self.body[:1024]