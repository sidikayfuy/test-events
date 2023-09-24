from rest_framework import serializers
from django.contrib.auth.models import User
from events_site.models import Event, CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'username', 'password', 'name', 'birthdate')
        read_only_fields = ('id',)
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'write_only': True},
            'last_name': {'write_only': True},
            'username': {'write_only': True},
        }

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            birthdate=validated_data['birthdate'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def get_name(self, obj):
        return str(obj)


class EventSerializer(serializers.ModelSerializer):
    participants = CustomUserSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'title', 'text', 'date', 'creator_id', 'participants')
        read_only_fields = ('id', 'creator_id')

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['creator'] = user
        event = Event.objects.create(**validated_data)
        event.participants.add(user)
        return event
