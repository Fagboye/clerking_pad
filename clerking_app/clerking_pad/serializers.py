from rest_framework import serializers
from .models import Patient_Biodata, Clerking


# serializer for clerking
class ClerkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clerking
        fields = '__all__'

# serializer for im clerking 
class IM_ClerkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clerking
        exclude = ['past_surgical_history']


# serializer for surgery clerking
class Surgery_ClerkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clerking
        fields = '__all__'
        exclude = ['past_medical_history']





