from django.urls import path
from .views import *

urlpatterns = [
    path("country/<str:country_name>", DataByCountry.as_view(), name ="Data by Country"),
    path("score-range/", DataByLaddderScoreRange.as_view(), name ="Data by ladder score range")
]