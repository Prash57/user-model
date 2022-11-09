from django.forms import ModelForm
from .models import Profile, Message, Identification, Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'username', 'bio',
                  'location', 'profile_image', 'phone', 'email', 'dob', 'gender']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['body']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)


class IdentificationForm(ModelForm):
    class Meta:
        model = Identification
        # fields = '__all__'
        fields = ['aadhar', 'aadhar_image']

    def __init__(self, *args, **kwargs):
        super(IdentificationForm, self).__init__(*args, **kwargs)

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
