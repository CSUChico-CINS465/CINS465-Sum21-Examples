from django.db import models

# Create your models here.


class SuggestionModel(models.Model):
    suggestion = models.CharField(
        max_length=240
    )

    def __str__(self):
        return str(self.id) + " " + self.suggestion
