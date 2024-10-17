from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# importing the models and serializers
from .models import *
from .serializers import *


from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound, PermissionDenied



#work flow for creating a internal medicine clerking
class IM_Clerking_View(generics.CreateAPIView):
    queryset = Clerking.objects.all()
    serializer_class = IM_ClerkingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except Exception as e:
            raise NotFound(detail=f"Error creating internal medicine clerking: {str(e)}")

#work flow for creating a surgery clerking
class Surgery_Clerking_View(generics.CreateAPIView):
    queryset = Clerking.objects.all()
    serializer_class = Surgery_ClerkingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except Exception as e:
            raise NotFound(detail=f"Error creating surgery clerking: {str(e)}")

#work flow to get all the clerking of a particular user
class Clerking_View_List(generics.ListAPIView):
    queryset = Clerking.objects.all()
    serializer_class = ClerkingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Clerking.objects.filter(user=user)

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

#work flow to get a single clerking, update and delete a particular clerking of a particular user
class Clerking_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clerking.objects.all()
    serializer_class = ClerkingSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise PermissionDenied("You do not have permission to access this clerking.")
        return obj

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PermissionDenied as e:
            return Response({'error': str(e)}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            updated_data = serializer.data
            return Response(updated_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)














