from django.db import models
from datetime import datetime

# Create your models here.

#need to migrate after changing or creating new model (it will migrate to the data base)
# Post models to store blogs in database
# admin username - admin
# e mail - admin@gmail.com
# password - admin
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=10000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)