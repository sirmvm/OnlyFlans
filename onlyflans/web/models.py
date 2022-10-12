
from unittest.util import _MAX_LENGTH
import uuid
from django.db import models

BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))


# Create your models here.
class Flan(models.Model):
    flan_uuid= models.UUIDField()
    id= models.AutoField(primary_key=True)
    name= models.CharField (max_length=64)
    description=models.TextField()
    image_url=models.URLField()
    slug=models.SlugField()
    is_private=models.BooleanField()
    price=models.IntegerField()
    


class ContactForm(models.Model):
    contact_form_uuid=models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email=models.EmailField()
    customer_name=models.CharField(max_length=64)
    message= models.TextField()
