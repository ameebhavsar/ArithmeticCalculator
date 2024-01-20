from django.db import models


class Input(models.Model):
    input_a = models.IntegerField()
    input_b = models.IntegerField()
    pub_date = models.DateTimeField("date published")
