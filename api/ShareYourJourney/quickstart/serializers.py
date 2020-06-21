from django.contrib.auth.models import Group, User
from rest_framework import serializers

from quickstart.models import Profile, Country, City, Post, CityRating


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups', 'profile']
        depth = 1


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'city_set']
        depth = 1


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['address', 'user', 'phone_number', 'age', 'sex', 'profile_picture', 'description', 'country_origin']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name', 'country_id']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author_id', 'title', 'text', 'created_date', 'city_id']


class CityRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityRating
        fields = ['city_id', 'night_life', 'sights', 'transportation', 'food', 'hospitality', 'crime_rate']
