from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Person
from .serializers import DataSerializer
# Create your views here.

@api_view(['GET'])
def getData(request):
    datas = Person.objects.all()

    serializer = DataSerializer(datas, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def saveData(request):
    serializer = DataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data )