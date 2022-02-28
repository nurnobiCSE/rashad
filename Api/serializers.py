from rest_framework import serializers

from Api.models import *

class skilSerializer(serializers.ModelSerializer):
    class Meta:
        model = skilModel
        fields = ['id','name','description','creator','progress_rate','ReleasDate']

class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = projectModel
        fields = ['id','title','description','image','previewLink','sourceLink','ReleasDate']