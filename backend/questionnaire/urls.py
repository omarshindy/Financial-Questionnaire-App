from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
from .api import RegisterApi, SectionQuestionListApi, BusinessPlanAPI, BusinessPlanQuestionsAPI


router = routers.DefaultRouter()
router.register('ping', views.PingViewSet, basename="ping")

urlpatterns = [
    # path('api/userplansquestion', userPlansQuestionsAPI.as_view(), name='user_plans_questions'),
    path('api/planquestions', BusinessPlanQuestionsAPI.as_view(), name='plan_questions'),
    path('api/createbp', BusinessPlanAPI.as_view(), name='business_plan'),
    path('api/<str:section_name>/questions',SectionQuestionListApi.as_view(), name='section_question_list'),
    path('api/register', RegisterApi.as_view(), name = 'registerapi'),
    path('api/token/access/', TokenRefreshView.as_view(), name='token_get_access'),
    path('api/token/both/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/', include(router.urls))
]

