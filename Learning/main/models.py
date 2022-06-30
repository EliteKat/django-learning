from django.db import models


class PBoard(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = 'PBoard'
        verbose_name_plural = 'PB fields'


