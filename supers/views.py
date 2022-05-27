from math import prod
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super
from supers import serializers

# Create your views here.
@api_view(['GET','POST'])
def super_list(request):
    
    if  request.method == 'GET':
     supers = Super.objects.all()
     serializer = SuperSerializer(supers,many=True)
     return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
