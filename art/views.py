from django.shortcuts import render
from rest_framework import viewsets
from .models import Student, Artwork
from .serializers import StudentSerializer, ArtworkSerializer
from rest_framework.permissions import IsAuthenticated


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ArtworkViewSet(viewsets.ModelViewSet):
    # queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Artwork.objects.filter(owner=self.request.user)
