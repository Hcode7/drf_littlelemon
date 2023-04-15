from rest_framework import serializers
from .models import *

class menuSerializers(serializers.ModelSerializer):
    class Meta:
        model = menu
        fields = '__all__'