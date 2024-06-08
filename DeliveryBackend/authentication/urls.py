from django.urls import path
from .views import CustomerRegistration, RiderRegistration
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("token/", jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('signup/', CustomerRegistration.as_view(), name='signup'),
    path('rider/signup/', RiderRegistration.as_view(), name='rider-signup'),

]

