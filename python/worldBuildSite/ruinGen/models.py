import datetime

from django.db import models
from django.utils import timezone

class RuinName(models.Model):
    ruinName_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.ruinName_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    ruinName = models.ForeignKey(RuinName, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class RuinedPlaces(models.Model):
    ruinName = models.ForeignKey(RuinName, on_delete=models.CASCADE)
    placeName_text = models.CharField(max_length=200)
    rStruct = models.CharField(max_length=50)
    yRuin = models.CharField(max_length=50)
    rInhab = models.CharField(max_length=50)
    longRuin = models.CharField(max_length=50)
    rCondition = models.CharField(max_length=50)
    def __str__(self):
        return self.placeName_text