from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="datastory"),
    path("api/chat/", views.chat, name="datastory_chat"),
    path("api/reset/", views.reset, name="datastory_reset"),
    path("api/schema/", views.schema, name="datastory_schema"),
    path("api/query/", views.run_query, name="datastory_query"),
]
