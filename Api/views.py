from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
# Create your views here.
def home(request):
    return render(request,"home.html")


class skilApi(APIView):
    def get(self,request, format=None):
        queryset = skilModel.objects.all()
        serializer = skilSerializer(queryset,many=True)
        return Response(serializer.data)

class projectModelApi(APIView):
    def get(self,request,format=None):
        queryset = projectModel.objects.all()
        serializer = ProjectModelSerializer(queryset,many=True)

        return Response(serializer.data)