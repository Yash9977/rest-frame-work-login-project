from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .Serializers import *
import json
from rest_framework import viewsets,generics
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class Generics_View(generics.ListAPIView,generics.ListCreateAPIView):
    
    queryset = student.objects.all()
    serializer_class= studentserializers

class Generics_View1(generics.UpdateAPIView,generics.DestroyAPIView):
    
    queryset = student.objects.all()
    serializer_class = studentserializers
    lookup_field='id'

class studentAPI (APIView):
    def get(self,request):
       print(request.GET)
       student_obj =student.objects.all()
       serializers = studentserializers(student_obj,many=True)
       return Response({'status':400 ,'payload':serializers.data , 'message':'student'})
       
    def post(self,request):
       
       serializers = studentserializers(data=request.data)
       if not serializers.is_valid():
           print(serializers.errors)
           return Response({'status':100,'errors':serializers.errors,'message':'not valid user '})
       serializers.save()
       return Response({'status':101 ,'payload':serializers.data , 'message':'student new entery'})
    
    def patch(self,request,id):
        
        try: 
            student_obj =student.objects.get(id=id)
            serializers = studentserializers(student_obj,data=request.data,partial=True)
            if not serializers.is_valid():
                print(serializers.errors)
                return Response({'status':100,'errors':serializers.errors,'message':'not valid user '})
            serializers.save()
            return Response({'status':101 ,'payload':serializers.data , 'message':'student updated'})
        
        except Exception as e:
            return Response({'status':500,'message':'invalid id'})
   
    def put(self,request,id):
       
        try:
            print(request.body)
            student_obj =student.objects.get(id=id)
            serializers = studentserializers(student_obj,data=json.loads(request.body))
            if not serializers.is_valid():
                print(serializers.errors)
                return Response({'status':100,'errors':serializers.errors,'message':'not valid user '})
            serializers.save()
            return Response({'status':101 ,'payload':serializers.data , 'message':'student updated'})
        
        except Exception as e:
            return Response({'status':500,'message':'invalid id'})

class register(APIView):
    def post(self,request):
        serializers = Userserializers(data=request.data)
        if not serializers.is_valid():
            print(serializers.errors)
            return Response({'status':100,'errors':serializers.errors,'message':'not valid user '})
        serializers.save()
        user=User.objects.get(username=serializers.data['username'])
        refresh = RefreshToken.for_user(user)
        return Response({'status':1 ,'refresh':str(refresh), 'access':str(refresh.access_token),'message':'student register'})
           