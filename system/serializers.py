from rest_framework import serializers

from .models import Region, PeopleCategory, People


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'title', 'short_description', 'description', 'center_city', 'center_lon', 'center_lat')
        read_only_fields = ('id',)


class PeopleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PeopleCategory
        fields = ('id', 'title', 'color')
        read_only_fields = ('id',)


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ('id', 'title', 'region', 'category', 'short_description',
                  'description', 'count', 'radius', 'map_lon', 'map_lat')
        read_only_fields = ('id',)



