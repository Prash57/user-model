from rest_framework import serializers
from base.models import Profile, Message, Group, Identification


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class IdentificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Identification
        fields = '__all__'