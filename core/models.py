from django.db import models

class TimeStampModel(models.Model):
  """
  An abstract base class model that provides self-
  . fields.
  updating ``created`` and ``modified``
  """
  created = models.DateTimeField(auto_now_add=True, null=True)
  modified = models.DateTimeField(auto_now=True, null=True)
  
  class Meta:
    abstract = True