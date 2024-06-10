
from django.urls import path
from .views import SignUp,UserLogin,SearchView

urlpatterns = [
    path('register/', SignUp.as_view()),
    path('login/', UserLogin.as_view()),
    path('searchuser/', SearchView.as_view()),
]
