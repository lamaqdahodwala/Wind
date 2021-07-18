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
    GenericViewSet
):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    pass

    @action(detail=True, methods=['GET'])
    def get_single_question(self, req, pk):
        question = self.get_object()
        ser = QuestionSerializer(question)
        return Response(ser.data)