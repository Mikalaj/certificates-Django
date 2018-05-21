from .views import Baptism, Wedding
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BaptismSerializer


@api_view(['GET', 'POST'])
def api_baptism_list(request, format=None):
    """
    List all code baptisms, or create a new baptism.
    """
    if request.method == 'GET':
        baptisms = Baptism.objects.all()
        serializer = BaptismSerializer(baptisms, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BaptismSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def api_baptism_detail(request, pk, format=None):
    """
    Retrieve, update or delete a baptism.
    """
    try:
        baptism = Baptism.objects.get(pk=pk)
    except Baptism.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BaptismSerializer(baptism)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BaptismSerializer(baptism, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        baptism.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
