from rest_framework import *
from rest_framework import serializers  
from .models import *
from django.contrib.auth.models import User
class studentserializers(serializers.ModelSerializer):
    
    class Meta:
        model=student
        fields=['name','ade']

class Userserializers(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=['username','password']        
