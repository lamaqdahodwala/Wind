from django.contrib.auth.models import User
from ..models import Question, Answer
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers



class AnswerSerializer(ModelSerializer):
    user = serializers.HyperlinkedRelatedField(default=serializers.CurrentUserDefault(), queryset=User.objects.all(), view_name='user-detail')
    question = serializers.RelatedField()


class QuestionSerializer(ModelSerializer):
    op = serializers.HyperlinkedRelatedField(default=serializers.CurrentUserDefault(), queryset=User.objects.all(), view_name='user-detail')
    class Meta:
        model = Question
        fields = ("op", "title", "body", 'id')


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)