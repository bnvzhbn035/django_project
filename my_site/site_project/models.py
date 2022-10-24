from django.db import models


class Teachers(models.Model):
    first_name = models.CharField(null=False, max_length=50)
    last_name = models.CharField(null=True, max_length=50)
    subject = models.ForeignKey("Subjects", on_delete=models.CASCADE)


class Subjects(models.Model):
    name = models.CharField(null=False, max_length=20)
    description = models.CharField(null=False, max_length=500)
    duration = models.IntegerField(null=True)
    start_date = models.DateTimeField(null=True)


class Marks(models.Model):
    amount = models.CharField(null=False, max_length=2)

