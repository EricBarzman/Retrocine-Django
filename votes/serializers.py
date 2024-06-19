from rest_framework import serializers
from .models import Vote, Avatar


class Avatar_serializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = ('id', 'label', 'get_image')