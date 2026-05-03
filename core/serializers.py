from rest_framework import serializers
from .models import Prompt, Image

class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = ["id", "text", "created_at"]

class ImageSerializer(serializers.ModelSerializer):
    prompt = PromptSerializer(read_only=False, many=False)

    class Meta:
        model = Image
        fields = ["id", "image", "uploaded_at", "prompt"]

