from django.urls import path, include

urlpatterns = [
    path("", include("core.urls")),
    path("datastory/", include("datastory.urls")),
    path("anotherurlshortner/", include("shortener.urls")),
    path("market_analyst/", include("market_analyst.urls")),
    path("inventory_whisperer/", include("inventory_whisperer.urls")),
]
