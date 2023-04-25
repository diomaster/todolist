from django.db import models
from django.utils import timezone
# Create your models here.


class List(models.Model):

      def __str__ (self):
        return self.title

      title = models.CharField(max_length=255)
      details = models.TextField()
      date = models.DateTimeField(default=timezone.now)

