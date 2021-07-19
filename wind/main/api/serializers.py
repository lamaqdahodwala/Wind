from django.contrib.auth.models import User
from ..models import Question
from rest_framework.serializers import  ModelSerializer
from rest_framework import serializers
class QuestionSerializer(ModelSerializer):
    op = serializers.SlugRelatedField(many=False, read_only=True, slug_field='id')
    class Meta:
        model = Question
        fields = ('op', 'title', 'body')