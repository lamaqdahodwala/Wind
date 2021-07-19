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
    GenericViewSet,
):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    @action(methods=["GET"], url_path="get_user_pk", detail=False)
    def get_user_pk(self, req):
        if req.user.is_authenticated:
            return Response(data={"pk": req.user.pk})
        else:
            return Response(data={"pk": "null"})
