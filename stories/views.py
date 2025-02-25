from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Story
from .serializers import StorySerializer

class StoryListView(APIView):
    def get(self, request, format=None):
        stories = Story.objects.all()
        serializer = StorySerializer(stories, many=True)
        return Response(serializer.data)