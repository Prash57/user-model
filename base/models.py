from django.db import models
from django.contrib.auth.models import User
import uuid
import pathlib
from datetime import datetime
# Create your models here.

GENDER_TYPE = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
)

GROUP_TYPE = (
    ('Social', 'Social'),
    ('Professional', 'Professional'),
    ('Community', 'Community'),
)


# for profiles image renaming
def profile_rename_upload(instance, filename):
    fpath = pathlib.Path(filename)
    # new_fname = str(datetime.now().strftime("%Y%m%d-%H%M%S"))
    new_fname = str(datetime.now())
    return f"profiles_img/{new_fname}{fpath.suffix}"

# for aadhar images renaming


def aadhar_rename_upload(instance, filename):
    fpath = pathlib.Path(filename)
    # new_fname = str(datetime.now().strftime("%Y%m%d-%H%M%S"))
    new_fname = str(datetime.now())
    return f"aadhar_img/{new_fname}{fpath.suffix}"


class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    bio = models.CharField(max_length=300, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    profile_image = models.ImageField(
        blank=True, null=True, default=None, upload_to=profile_rename_upload)
    phone = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=55, blank=True, null=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_TYPE, max_length=10)

    def __str__(self):
        return self.username

    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url


class Message(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    sender = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    recipient = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True, related_name='messages')
    # name = models.CharField(max_length=100, blank=True, null=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:20]

    class Meta:
        ordering = ['is_read', '-created']


class Group(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    name = models.CharField(choices=GROUP_TYPE, max_length=15)

    def __str__(self):
        return self.name


class Identification(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    user = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    aadhar = models.IntegerField(null=True, blank=True)
    aadhar_image = models.ImageField(
        blank=True, null=True, default=None, upload_to=aadhar_rename_upload)

    def __str__(self):
        return str(self.aadhar)
