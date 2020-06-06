from django.db import models

class Galpan_character(models.Model):
    name = models.CharField(max_length=20)
    text = models.TextField(max_length=200)

    def __str__(self):
        return self.name
