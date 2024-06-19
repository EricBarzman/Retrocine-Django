from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Avatar
from .serializers import Avatar_serializer

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_avatars(request):
    avatars = Avatar.objects.all()
    serializer = Avatar_serializer(avatars, many=True)
    return Response(serializer.data)