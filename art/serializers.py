from rest_framework import serializers
from .models import Artwork, Student


class ArtworkSerializer(serializers.ModelSerializer):
    student_name = serializers.StringRelatedField(
        source='student',
        read_only=True
    )

    student_id = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(), source='student')

    class Meta:
        model = Artwork
        fields = ('id', 'title', 'artwork_image', 'price', 'publication_date',
                  'student_name', 'student_id', 'owner')


class StudentSerializer(serializers.ModelSerializer):
    artworks = ArtworkSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ('id', 'name', 'avatar', 'school',
                  'graduation_year', 'personal_story', 'artworks',)
