from django.contrib.auth.models import User
from ..models import Question, Answer
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)




class AnswerSerializer(ModelSerializer):
    user = UserSerializer(default=serializers.CurrentUserDefault())
    class Meta:
        model = Answer
        fields = ('user', 'question', 'body')

class QuestionSerializer(ModelSerializer):
    op = UserSerializer(default=serializers.CurrentUserDefault())
    answers = AnswerSerializer(many=True)
    class Meta:
        model = Question
        fields = ("op", "title", "body", 'id', 'answers')