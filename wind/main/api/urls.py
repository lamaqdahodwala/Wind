from . import views
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"question", views.QuestionViewSet, basename="question")

urlpatterns = router.urls + [
    path('answer/<int:qid>/create', views.CreateAnswerView.as_view(), name='createanswer')
]
