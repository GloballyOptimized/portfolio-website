from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="shortener"),
    path("api/shorten/", views.shorten, name="shortener_shorten"),
    path("api/info/", views.api_info, name="shortener_info"),
    path("api/stats/<str:code>/", views.stats_view, name="shortener_stats"),
    path("<str:code>", views.redirect_url, name="shortener_redirect"),
]
