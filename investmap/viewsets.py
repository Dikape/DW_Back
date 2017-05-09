from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import InvestMapObjectSerializer, InvestMapPointSerializer, ObjectHolderSerializer
from .models import InvestMapObject, InvestMapPoint, ObjectHolder


class InvestMapObjectViewSet(viewsets.ModelViewSet):
    model = InvestMapObject
    queryset = InvestMapObject.objects.all()
    serializer_class = InvestMapObjectSerializer


class InvestMapPointViewSet(viewsets.ModelViewSet):
    model = InvestMapPoint
    queryset = InvestMapPoint.objects.all()
    serializer_class = InvestMapPointSerializer


class ObjectHolderViewSet(viewsets.ModelViewSet):
    model = ObjectHolder
    queryset = ObjectHolder.objects.all()
    serializer_class = ObjectHolderSerializer


