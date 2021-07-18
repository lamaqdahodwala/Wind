from .serializers import QuestionSerializer
from ..models import Question
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

class QuestionViewSet(
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    pass