from .models import Baptism, Wedding, Clergy
from .serializers import BaptismSerializer, WeddingSerializer, ClergySerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse



class BaptismList(generics.ListCreateAPIView):
    queryset = Baptism.objects.all()
    serializer_class = BaptismSerializer


class BaptismDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Baptism.objects.all()
    serializer_class = BaptismSerializer


class WeddingList(generics.ListCreateAPIView):
    queryset = Wedding.objects.all()
    serializer_class = WeddingSerializer


class WeddingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wedding.objects.all()
    serializer_class = WeddingSerializer


class ClergyList(generics.ListAPIView):
    queryset = Clergy.objects.all()
    serializer_class = ClergySerializer


class ClergyDetail(generics.RetrieveAPIView):
    queryset = Clergy.objects.all()
    serializer_class = ClergySerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'clergies': reverse('clergy-list', request=request, format=format),
        'baptisms': reverse('baptism-list', request=request, format=format),
        'weddings': reverse('wedding-list', request=request, format=format)
    })
