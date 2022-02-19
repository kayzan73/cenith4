from django.db import models


#
# Mixins
#


# NamedModelMixin
# Mixin for models with a name field.
class NamedModelMixin(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        abstract = True


# ShortNamedModelMixin
# Mixin for named models with a short_name field.
class ShortNamedModelMixin(NamedModelMixin):
    short_name = models.CharField(max_length=100)

    def __str__(self):
        return "{},{}".format(self.name, self.short_name)

    class Meta:
        abstract = True


# TimeStampedModelMixin
# Mixin for models using timestamps for creation and last modification.
class TimeStampedModelMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
