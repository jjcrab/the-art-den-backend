from django.urls import path, include
from student_users import views

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken'))
]
