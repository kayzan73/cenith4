from django.db import models
from common.models import NamedModelMixin, TimeStampedModelMixin


class Organization(NamedModelMixin, TimeStampedModelMixin):

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('organization_details', kwargs={'pk': self.id})


class OrganizationalUnit(NamedModelMixin, TimeStampedModelMixin):
    organization = models.ForeignKey(Organization,
                                     on_delete=models.CASCADE,
                                     related_name="organizational_units")

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('organizational_unit_details', kwargs={'pk': self.id})
