from rest_framework import serializers
from .models import Address

'''
Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes 
that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, 
allowing parsed data to be converted back into complex types, after first validating the incoming data.
'''
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        '''
        extra_kwargs = {
            'user': {'validators': []},
        }

        def create(self, validated_data):
            return Address.objects.create(**validated_data)
        '''
        '''
        instance is whats currently exist in database.
        validated_data is the incoming data after validation succeeded
        '''
        '''
        def update(self, instance, validated_data):
            instance.address1 = validated_data.get('address1', instance.address1)
            instance.address2 = validated_data.get('address2', instance.address2)
            instance.city = validated_data.get('city', instance.city)
            instance.state = validated_data.get('state', instance.state)
            instance.postal_code = validated_data.get('postal_code', instance.postal_code)
            instance.country = validated_data.get('country', instance.country)
            instance.address_type = validated_data.get('address_type', instance.address_type)
            instance.save()
            return instance
        '''