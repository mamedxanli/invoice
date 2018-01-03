from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_countries.fields import CountryField


class BaseMetaData(models.Model):
    """ MetaData model """

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseAddress(BaseMetaData):
    """ Address model """

    country = CountryField(blank_label=_('(Select Country)'))
    county = models.CharField(_('county'), max_length=50, blank=True)
    city = models.CharField(_('city'), max_length=90)
    address_line1 = models.CharField(_('address line 1'), max_length=90)
    address_line2 = models.CharField(_('address line 2'), max_length=90, blank=True)
    name = models.CharField(_('name'), max_length=90)
    phone = models.IntegerField(_('phone'), blank=True)
    email = models.EmailField(_('email'), max_length=90, blank=True)

    def get_full_address(self):
        """
        Return the all the address info.
        """
        return ", ".join([x for x in [self.address_line_1,
                         self.address_line_2, self.city, self.county,
                         self.country] if x]),

    def __str__(self):
        """
        Return the both address lines, with a space in between.
        """
        if self.address_line2:
            return ", ".join([self.address_line1, self.address_line2])
        else:
            return self.address_line1

    class Meta:
        abstract = True
