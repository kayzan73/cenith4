from django.db import models


#
# Mixins
#


# HierarchicalModelMixin
# Mixin for models with parent-child-relationship.
class HierarchicalModelMixin(models.Model):
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               related_name="children",
                               null=True,
                               blank=True)

    class Meta:
        abstract = True


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
    short_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "{}, {}".format(self.name, self.short_name)

    class Meta:
        abstract = True


# TimeStampedModelMixin
# Mixin for models using timestamps for creation and last modification.
class TimeStampedModelMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
