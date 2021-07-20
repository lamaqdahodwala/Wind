from django.contrib.auth.models import User
from ..models import Question
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers



class QuestionSerializer(ModelSerializer):
    op = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Question
        fields = ("op", "title", "body")
