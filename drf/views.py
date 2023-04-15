from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class menuItemView(generics.ListCreateAPIView):
    queryset = menu.objects.all()
    serializer_class = menuSerializers



class SingleItemView(generics.DestroyAPIView,generics.RetrieveUpdateAPIView):
    queryset = menu.objects.all()
    serializer_class = menuSerializers

@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message":"Some secret message"})