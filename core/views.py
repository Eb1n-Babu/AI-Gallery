from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Prompt,Image

from .serializers import PromptSerializer, ImageSerializer


class PromptViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer
    permission_classes = [AllowAny]

class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [AllowAny]

