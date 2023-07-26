from rest_framework import serializers
from .models import Polling


class PollingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'polling_text',
            'pub_date',
        )
        model = Polling