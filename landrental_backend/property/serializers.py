from rest_framework import serializers

from .models import Property

class PropertiesListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Property
        fields = ('id', 'title', 'image_url', 'price', )
