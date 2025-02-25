from rest_framework import serializers
from .models import Story

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'header', 'description', 'content', 'image', 'link_text', 'link_icon']