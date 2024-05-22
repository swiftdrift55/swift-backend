from django.urls import path
from .views import RiderSignupView, UserSignupView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("token/", jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('rider/signup/', RiderSignupView.as_view(), name='rider-signup'),
]

