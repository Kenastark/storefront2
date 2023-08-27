from decimal import Decimal
from store.models import Product, Collection
from rest_framework import serializers

class CollectionSerializer(serializers.Serializer):
    id =serializers.IntegerField()
    title = serializers.CharField(max_length=255)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [ 'id', 'title', 'unit_price', 'price_with_tax', 'collection']

    # #SerializerMethodField a method will be defined and will return the result for this field
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    collection = serializers.HyperlinkedRelatedField(
        queryset =Collection.objects.all(),
        view_name='collection-detail'
    )

    #type annotation is used to enable intellisense
    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
     