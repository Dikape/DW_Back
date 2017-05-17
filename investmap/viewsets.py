from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import InvestmentObjectSerializer, InvestMapPointSerializer, ObjectHolderSerializer
from .models import InvestmentObject, InvestMapPoint, ObjectHolder


class InvestmentObjectViewSet(viewsets.ModelViewSet):
    model = InvestmentObject
    queryset = InvestmentObject.objects.all()
    serializer_class = InvestmentObjectSerializer


class InvestMapPointViewSet(viewsets.ModelViewSet):
    model = InvestMapPoint
    queryset = InvestMapPoint.objects.all()
    serializer_class = InvestMapPointSerializer


class ObjectHolderViewSet(viewsets.ModelViewSet):
    model = ObjectHolder
    queryset = ObjectHolder.objects.all()
    serializer_class = ObjectHolderSerializer


