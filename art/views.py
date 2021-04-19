from django.shortcuts import render
from rest_framework import viewsets
from .models import Student, Artwork
from .serializers import StudentSerializer, ArtworkSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ArtworkViewSet(viewsets.ModelViewSet):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
