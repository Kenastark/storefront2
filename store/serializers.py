from decimal import Decimal
from store.models import Product, Collection
from rest_framework import serializers

class CollectionSerializer(serializers.ModelSerializer):
    model = Collection
    fields = ['id', 'title']
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [ 'id', 'title', 'unit_price', 'price_with_tax', 'collection']

    # #SerializerMethodField a method will be defined and will return the result for this field
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    """ collection = serializers.HyperlinkedRelatedField(
        queryset =Collection.objects.all(),
        view_name='collection-detail'
    ) """

    #type annotation is used to enable intellisense
    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
     

# Overriding the validate method in our serializer
    # def validate(self, data):
    #     if data['passowrd'] != data['confirm password']:
    #         return serializers.ValidationError('Passwords do not match')
        
    #     return data