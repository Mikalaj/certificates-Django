from rest_framework import serializers
from .models import Baptism, Wedding, Clergy


class BaptismSerializer(serializers.HyperlinkedModelSerializer):
    # priest = ClergySerializer()
    # priest = serializers.ReadOnlyField(source='clergy')

    class Meta:
        model = Baptism
        fields = ['url', 'id', 'date', 'number', 'priest', 'certificate',
                  'baptized_name', 'baptized_middle_name', 'baptized_surname',
                  'godfather', 'godmother', 'saint_name', 'saint_date']


class WeddingSerializer(serializers.HyperlinkedModelSerializer):
    # priest = ClergySerializer()

    class Meta:
        model = Wedding
        fields = ['date', 'number', 'priest', 'certificate',
                  'fiance_name', 'fiance_middle_name', 'fiance_surname',
                  'fiancee_name', 'fiancee_middle_name', 'fiancee_surname',
                  'witness1', 'witness2']


class ClergySerializer(serializers.HyperlinkedModelSerializer):
    # baptisms = serializers.HyperlinkedRelatedField(many=True, view_name='baptism-detail', read_only=True)
    # baptisms = serializers.HyperlinkedRelatedField()
    class Meta:
        model = Clergy
        fields = ['url', 'id', 'dignity', 'name',]

