from .views import Baptism, Wedding
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from .serializers import BaptismSerializer


@csrf_exempt
def api_baptism_list(request):
    """
    List all code baptisms, or create a new baptism.
    """
    if request.method == 'GET':
        baptisms = Baptism.objects.all()
        serializer = BaptismSerializer(baptisms, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BaptismSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def api_baptism_detail(request, pk):
    """
    Retrieve, update or delete a baptism.
    """
    try:
        baptism = Baptism.objects.get(pk=pk)
    except Baptism.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BaptismSerializer(baptism)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BaptismSerializer(baptism, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        baptism.delete()
        return HttpResponse(status=204)
