from rest_framework import generics,status
from .serializers import WorldHappinessReportSerializer
from .models import WorldHappinessReport
from rest_framework.response import Response

class DataByCountry(generics.ListAPIView):
    serializer_class = WorldHappinessReportSerializer

    def get_queryset(self):
        country_name=self.kwargs.get("country_name",None)
        if country_name.lower():
           country_name=country_name.capitalize()
        return WorldHappinessReport.objects.filter(countryName=country_name)

class DataByLaddderScoreRange(generics.ListAPIView):
    serializer_class = WorldHappinessReportSerializer

    def get_queryset(self):
        range_from = self.request.query_params.get('from', None)
        range_to=self.request.query_params.get('to', None)
        return WorldHappinessReport.objects.filter(ladderScore__gte=range_from,ladderScore__lte=range_to)


