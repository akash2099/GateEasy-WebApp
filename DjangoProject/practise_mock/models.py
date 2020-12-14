from django.db import models
from jsonfield import JSONField


class MockTest(models.Model):
    Department = models.CharField(max_length=250)
    subject = models.CharField(max_length=500)
    mock_no = models.IntegerField()
    mock = models.JSONField(default=dict)

    def __str__(self):
         return self.Department+ " " + self.subject + "( "+str(self.mock_no)+" )"