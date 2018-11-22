import uuid

from django.db import models
from django.utils import timezone


class Blog(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description =  models.TextField(max_length=2000)
    pub_date = models.DateTimeField(default=timezone.now)
