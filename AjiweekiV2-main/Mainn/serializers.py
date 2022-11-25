from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class FormSerializer(serializers.Serializer):

    class Meta:
        model=Form
        fields="__all__"

class QuestionsSerializer(serializers.Serializer):
    
    class Meta:
        model=Questions
        fields="__all__"


class UserResponseSerializer(serializers.Serializer):

    class Meta:
        model=UserResponse
        fields="__all__"

class QuestionChoiceSerializer(serializers.Serializer):
    class Meta:
        model=QuestionChoice
        fields="__all__"
