from rest_framework import viewsets
from rest_framework.response import Response
from .models import UserProfile
from .models import UserEducation
from . import serializers
from core.permissions import IsOwnerOrReadOnly


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer
    # permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def retrieve(self, request, format=None, **kwargs):
        userprofile = self.get_object()
        user_serializer = serializers.UserProfileSerializer(userprofile)
        user_education_serializer = serializers.UserEducationSerializer(userprofile.user_education.all(),many=True)

        return Response({
            'userprofile': user_serializer.data,
            'education': user_education_serializer.data,
        })
