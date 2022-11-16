from django.db import models
from base.models import Profile
import uuid

# Create your models here.


class Feed(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    user = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)
    post = models.TextField()
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.post[0:20]


class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

