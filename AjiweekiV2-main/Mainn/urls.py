from django.urls import path, include
from Account.views import *
from Mainn.views import *
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from .views  import *




app_name = 'Mainn'


router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),


    path('form/', FormAPIView.as_view(),name='FORM'),
    path('question/', QuestionsAPIView.as_view(), name="QUESTIONS"),
    path('userresponse/', UserResponseAPIView.as_view(), name="USERRESPONSE"),
    #path('questionchoice/', QuestionChoiceAPIView.as_view(), name="QUESTIONCHOICE"),
    path('userwiseresponse/', UserwiseResponseAPIView.as_view(),name="USERWISERESPONSE"),
    path('questionanswer/', QuestionanswerAPIView.as_view(),name = "QUESTIONANSWER"),


]
