from django.db import models
from django.utils import timezone
# Create your models here.


LIST_CHOICES = (
        ('work', 'WORK'),
        ('school', 'SCHOOL'),
        ('videos', 'VIDEOS'),
      )


class List(models.Model):

      def __str__ (self):
        return self.title
      

      title = models.CharField(max_length=255)
      details = models.TextField()
      date = models.DateTimeField(default=timezone.now)
      type = models.CharField(max_length=6, choices=LIST_CHOICES, default='work')
