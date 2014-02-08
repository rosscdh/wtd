from django.db import models


class Domain(models.Model):
    domain = models.CharField(max_length=255)


class Page(models.Model):
    domain = models.ForeignKey('core.Domain')
    part = models.CharField(max_length=255, db_index=True)
    body = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        # latest first
        ordering = ['-id']