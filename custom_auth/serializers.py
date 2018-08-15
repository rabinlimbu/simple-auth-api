from django.contrib.auth.models import User, Group
from rest_framework import serializers, status
from .models import Profile

# first we define the serializers
'''
Think of the Meta class as a container for configuration attributes of the outer class.
In peewee (and also Django), the attributes of a class (for those that inherit from Model)
are expect to be fields that correspond to their counterparts in the database.
How then to add attributes that aren't database fields? The Meta class is the container for
these non-field attributes.
As new instances of your outer class are created, the class constructor will look to the
Meta attribute for specific configuration details.
'''


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        # fields = ('bio','birth_date','location','gender')
        # user = serializers.ReadOnlyField(source='owner.username')
        extra_kwargs = {
            'user': {'validators': []},
        }


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'last_login', 'date_joined', 'profile')

    def update(self, instance, validated_data):
        profile_data = validated_data.pop("profile")

        if hasattr(instance, 'profile'):
            try:
                profile = instance.profile
            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            instance.first_name = validated_data.get('first_name', instance.first_name)
            instance.last_name = validated_data.get('last_name', instance.last_name)
            instance.save();

            '''
            profile.id = profile_data.get('id')
            profile.user = profile_data.get(
                'user',
                profile.user
            )
            '''
            profile.bio = profile_data.get(
                'bio',
                profile.bio
            )
            profile.birth_date = profile_data.get(
                'birth_date',
                profile.birth_date
            )
            profile.location = profile_data.get(
                'location',
                profile.location
            )

            profile.save()
        else:
            user = profile_data.get('user')
            Profile.objects.create(**profile_data)
            profile = profile_data

        return profile


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
