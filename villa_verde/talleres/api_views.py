from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import Taller
from .serializers import TallerSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Taller
from .serializers import TallerSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def proponer_taller(request):
    user = request.user

    if user.tipo != 'junta':
        return Response({'detail': 'Solo las Juntas de Vecinos pueden proponer talleres.'}, status=403)

    data = request.data.copy()
    data['estado'] = 'pendiente' 
    serializer = TallerSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def listar_talleres_api(request):
    talleres = Taller.objects.all()
    serializer = TallerSerializer(talleres, many=True)
    return Response(serializer.data)
