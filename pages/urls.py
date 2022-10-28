from django.urls import path
from .views import HomePageView, AboutPageView, NextPageView

urlpatterns = [
    path("", HomePageView.as_view(),name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("next/", NextPageView.as_view(), name="next")
]
