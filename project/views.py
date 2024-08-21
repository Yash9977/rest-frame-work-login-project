from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .Serializers import *
# Create your views here.

class studentAPI (APIView):
    def get(self,request):
       
       student_obj =student.objects.all()
       serializers = studentserializers(student_obj,many=True)
       return Response({'status':400 ,'payload':serializers.data , 'message':'student'})
       
    def post(self,request):
        pass
    def patch(self,request):
        pass
    def put(self,request):
        pass
    