from django.db import models

# Create your models here.


class Viewmap(models.Model):
    address = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.address}'

    class Meta:
        verbose_name_plural = "Viewmap"