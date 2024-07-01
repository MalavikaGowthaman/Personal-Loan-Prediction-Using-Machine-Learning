from django.db import models

# Create your models here.
class ckdModel(models.Model):

    Age=models.FloatField()
    Experience=models.FloatField()
    Income=models.FloatField()
    Family=models.FloatField()
    CCAvg=models.FloatField()
    Education=models.FloatField()
    Mortgage=models.FloatField()
    CDAccount=models.FloatField()
    OnlineAccount=models.FloatField()
