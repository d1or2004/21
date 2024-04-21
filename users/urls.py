from django.urls import path
from .views import SignUpPageView, LoginPageView, LandingPage
urlpatterns = [
    path('', LandingPage.as_view(), name='landing'),
    path('sign/', SignUpPageView.as_view(), name='sign'),
    path('login/', LoginPageView.as_view(), name='login'),
]
