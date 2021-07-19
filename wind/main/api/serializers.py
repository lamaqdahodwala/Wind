from django.contrib.auth.models import User
from ..models import Question
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)
class QuestionSerializer(ModelSerializer):
    op = UserSerializer()
    class Meta:
        model = Question
        fields = ("op", "title", "body", 'id')
