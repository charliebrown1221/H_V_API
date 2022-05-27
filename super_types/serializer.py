from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Super_type

class Super_typeSerializer(serializers.ModelSerializer):
    class Meta:
         model = Super_type
         fields = ['id','type']