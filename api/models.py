from django.db import models


# Create your models here.


class Bucketlist(models.Model):
    """This class represents the bucketlist model."""

    name = models.CharField(max_length=255, blank=False, unique=True)
    owner = models.ForeignKey('auth.User',
                              related_name='backetlists',
                              on_delete=models.CASCADE,
                              )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)
