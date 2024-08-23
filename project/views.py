from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .Serializers import *
import json
# Create your views here.

class studentAPI (APIView):
    def get(self,request):
       
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
   