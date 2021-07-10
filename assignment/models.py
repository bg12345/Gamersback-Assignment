from django.db import models

class WorldHappinessReport(models.Model):
    countryName=models.CharField(max_length=200,unique=True)
    rank=models.CharField(max_length=100,unique=True)
    ladderScore=models.CharField(max_length=200)
    healthyLifeExpectancy=models.CharField(max_length=200)
    generosity=models.CharField(max_length=200)
    gdp=models.CharField(max_length=200)

    def __str__(self):
        return self.countryName
