import json
from django.shortcuts import render

from .core.database import get_kpis, get_watchlist, get_projection_data


def dashboard(request):
    try:
        kpis       = get_kpis()
        watchlist  = get_watchlist()
        projection = get_projection_data()
    except Exception as e:
        kpis       = {}
        watchlist  = {"reorder": [], "slow_movers": []}
        projection = []

    return render(request, "inventory_whisperer/dashboard.html", {
        "active":     "inventory_whisperer",
        "kpis":       kpis,
        "watchlist":  watchlist,
        "projection": json.dumps(projection, default=str),
    })
