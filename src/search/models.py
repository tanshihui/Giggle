from django.db import models

# Create your models here.

class Search(models.Model):
    search_term = models.CharField(max_length=120, null=True, blank=True)
    search_suggest = models