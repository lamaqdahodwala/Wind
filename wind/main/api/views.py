from django.contrib.auth.models import User
from django.http.response import HttpResponseForbidden
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import QuestionSerializer, UserSerializer
from ..models import Answer, Question
from rest_framework.viewsets import GenericViewSet
from django.shortcuts import get_object_or_404
from rest_framework import mixins
from rest_framework.views import APIView

class QuestionViewSet(
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class CreateAnswerView(APIView):
    def post(self, req, qid):
        if req.user.is_authenticated:
            question = get_object_or_404(Question, pk=qid)
            Answer.objects.create(user=req.user, question=question, body=req.data['body'])
            return
        return HttpResponseForbidden()