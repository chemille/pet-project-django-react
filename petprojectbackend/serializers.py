from rest_framework import serializers
from .models import Pet

class PetSerializer(serializers.ModelSerializer):
    # inner class called Meta which will the metadata describing the model
    class Meta:
        # id is automatically added to the model
        model = Pet
        fields = ['id', 'name', 'description']

# Will be using this serializer when trying to return the model through our API