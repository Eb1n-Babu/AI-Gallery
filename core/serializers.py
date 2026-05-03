from rest_framework import serializers
from .models import Prompt, Image

class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = ["id", "text", "created_at"]

class ImageSerializer(serializers.ModelSerializer):
    prompt = PromptSerializer(read_only=True)
    prompt_id = serializers.PrimaryKeyRelatedField(
        queryset=Prompt.objects.all(),
        source="prompt",
        write_only=True
    )

    class Meta:
        model = Image
        fields = ["id", "image", "uploaded_at", "prompt", "prompt_id"]
