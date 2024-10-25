from django.shortcuts import render
from .models import WardrobeItem
from rest_framework import viewsets
from .serializers import WardrobeItemSerializer

class WardrobeItemViewSet(viewsets.ModelViewSet):
    queryset = WardrobeItem.objects.all()
    serializer_class = WardrobeItemSerializer
