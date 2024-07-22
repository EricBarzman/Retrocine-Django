from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Issue_Message, Topic
from .serializers import Topic_serializer, Issue_message_serializer

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_topics(request):
    topics = Topic.objects.all()
    serializer = Topic_serializer(topics, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def register_issue_message(request):
    issue = Issue_Message.objects.create(
        email = request.data.get('email'),
        content = request.data.get('content'),
        topic = Topic.objects.get(label=request.data.get('topic'))
    )
    issue.save()
    
    serializer = Issue_message_serializer(issue, many=False)
    return Response(serializer.data)