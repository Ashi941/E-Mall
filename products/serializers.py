from rest_framework import serializers
from .models import Product,Category

 
#convert all the table fields into json and vice versa 
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"
 
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"

