from django.urls import path, include
from Account.views import *
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from . import views
from Account.views import *





app_name = 'Account'


router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),


    path('signup/', SignupApiVew.as_view()),
    path('login/', LoginApiView.as_view(), name="LOGIN"),
    ]
