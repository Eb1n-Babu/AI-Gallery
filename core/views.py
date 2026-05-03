from rest_framework import viewsets
from .models import Prompt,Image

from .serializers import PromptSerializer, ImageSerializer


class PromptViewSet(viewsets.ModelViewSet):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

