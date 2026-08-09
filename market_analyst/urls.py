from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="market_analyst"),
    path("api/research/", views.research, name="market_analyst_research"),
    path("api/session/<str:session_id>/", views.session_detail, name="market_analyst_session"),
]
