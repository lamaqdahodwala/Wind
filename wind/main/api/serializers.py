from django.contrib.auth.models import User
from ..models import Question
from rest_framework.serializers import  ModelSerializer

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
    
    def create(self, validated_data):
        uid = validated_data.pop('op_id', None)
        user = User.objects.get(pk=uid)

        return Question.objects.create(user=user, **validated_data)
