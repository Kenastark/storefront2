from rest_framework import serializers

class ProductSerializer(serializers.Serializers):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    unit_price = serializers.DecimalFields(max_digits=6, decimal_places=2)