from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from control_acceso_app.auth.views import registration_view
urlpatterns = [
    path("register/", registration_view, name="register"),
    #path("login/", .as_view(), name="login"),
    #path("logout/", .as_view(), name="login"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

]

