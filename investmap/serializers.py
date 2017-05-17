from rest_framework import serializers

from .models import InvestmentObject, InvestMapPoint, ObjectHolder


class InvestmentObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentObject
        fields = ('id', 'name', 'description', 'price', 'address', 'metrics', 'contacts', 'object_holder', 'object_type', )
        read_only_fields = ('id',)


class InvestMapPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestMapPoint
        fields = ('id', 'investmap_object', 'map_lon', 'map_lat')
        read_only_fields = ('id', )


class ObjectHolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectHolder
        fields = ('id', 'title', 'address')
        read_only_fields = ('id',)