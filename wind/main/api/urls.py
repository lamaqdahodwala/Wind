from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'question', views.QuestionViewSet, basename='question')

urlpatterns = router.urls