from rest_framework import serializers
from .models import (
    Person,
    Address
)


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ('id' , 'city' , 'country')


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields =('id' ,'address' , 'first_name' , 'last_name' , 'age')



