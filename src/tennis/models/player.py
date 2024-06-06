from django.db import models


class TennisPlayer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    racket_brand = models.CharField(max_length=100)
    racket_model = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
