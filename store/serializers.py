from decimal import Decimal
from store.models import Product, Collection
from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')
    #SerializerMethodField a method will be defined and will return the result for this field
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    collection = serializers.StringRelatedField()

    #type annotation is used to enable intellisense
    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
     