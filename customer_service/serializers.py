from rest_framework import serializers
from .models import Issue_Message, Topic

class Topic_serializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'label', 'label_text')

class Issue_message_serializer(serializers.ModelSerializer):
    topic = Topic_serializer(many=False)
    class Meta:
        model = Issue_Message
        fields = ('id', 'email', 'topic', 'content', 'created_at')