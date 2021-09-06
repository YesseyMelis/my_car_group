from rest_framework import serializers

from apps.core.models import Car


class RetrieveCarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
