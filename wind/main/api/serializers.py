from django.contrib.auth.models import User
from ..models import Question
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class QuestionSerializer(ModelSerializer):
    op = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Question
        fields = ("op", "title", "body", 'id')
