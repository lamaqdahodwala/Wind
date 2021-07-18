from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import QuestionSerializer
from ..models import Question
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

class QuestionViewSet(
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    