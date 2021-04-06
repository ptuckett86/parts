from django.shortcuts import render

from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .serializers import *
from .models import *


class PartRequestViewSet(viewsets.ModelViewSet):
    serializer_class = PartRequestSerializer
    queryset = PartRequest.objects.all()


class DecisionViewSet(viewsets.ModelViewSet):
    serializer_class = DecisionSerializer
    queryset = Decision.objects.all()
