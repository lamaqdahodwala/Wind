from django.contrib.auth.models import User
from ..models import Question
from rest_framework.serializers import  ModelSerializer

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ('op', 'title', 'body')