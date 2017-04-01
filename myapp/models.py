from django.db import models

class Province(models.Model):
    province = models.CharField(max_length=30)

    def __str__(self):
        return self.province
