from rest_framework import serializers
from .models import Baptism, Wedding


class BaptismSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baptism
        fields = ['date', 'number', 'priest', 'certificate',
                  'baptized_name', 'baptized_middle_name', 'baptized_surname',
                  'godfather', 'godmother', 'saint_name', 'saint_date']
