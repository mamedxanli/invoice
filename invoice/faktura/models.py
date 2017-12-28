from django.db import models
from django.utils.translation import ugettext_lazy as _


class FakturaItem(BaseMetaData):
    """ FakturaItem model """

    description = models.CharField(_('Item Description'), blank=True),
    quantity = models.IntegerField(_('Quantity')),
    unit = models.CharField(_('Kg, Litres, Hours'), blank=True),
    rate = models.IntegerField(_('Rate or Price per unit')),
    amount = quantity * rate,
    currency = unit = models.CharField(_('Currency')),
