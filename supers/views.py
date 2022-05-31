from ast import Delete
from math import prod
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from super_types.models import Super_type
from .serializers import SuperSerializer
from .models import Super
from supers import serializers

# Create your views here.
@api_view(['GET'])
def type_dict(request):
  if  request.method == 'GET':
    types = Super_type.objects.all()
    custom_response_dictionary ={}
    for type in types:
     super = Super.objects.filter(type_id=type.id)
     type_serializer = SuperSerializer(super, many=True)
     custom_response_dictionary[type.type] = {
         'type': type_serializer.data
     }
    return Response(custom_response_dictionary)





@api_view(['GET','POST'])
def super_list(request):
    
    if  request.method == 'GET':
      
      super_company= request.query_params.get('type')
      print(super_company)

      supers = Super.objects.all()

      if super_company:
          supers = supers.filter(super_type__type=super_company)

      serializer = SuperSerializer(supers,many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def super_detail(request, pk):
    supers =get_object_or_404(Super,pk=pk)
    if request.method == 'GET':
        serializer =SuperSerializer(supers)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method =='PUT':
        serializer= SuperSerializer(supers,data=request.data)  
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)  
    elif request.method == 'DELETE':
        supers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
