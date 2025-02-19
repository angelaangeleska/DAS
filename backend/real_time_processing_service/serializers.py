import json

from rest_framework import serializers

def create_stock_serializer(model_class):
    class DynamicStockSerializer(serializers.ModelSerializer):
        class Meta:
            model = model_class
            fields = '__all__'
            extra_kwargs = {
                'date': {'format': '%Y-%m-%d'}
            }

    return DynamicStockSerializer

def serializer(message):
    return json.dumps(message).encode('utf-8')