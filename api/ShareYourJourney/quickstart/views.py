from django.contrib.auth.models import Group, User
from rest_framework import viewsets

from quickstart.serializers import ProfileSerializer, GroupSerializer, UserSerializer, CountrySerializer, \
    CitySerializer, PostSerializer, CityRatingSerializer
from quickstart.models import Profile, Country, City, Post, CityRating


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CityRatingViewSet(viewsets.ModelViewSet):
    queryset = CityRating.objects.all()
    serializer_class = CityRatingSerializer
