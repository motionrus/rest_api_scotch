from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .serializers import BucketlistSerializer
from .models import Bucketlist


class CreateView(generics.ListCreateAPIView):
    """This class defines the create """
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save(owner=self.request.user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
