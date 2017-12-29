from django.db import models
from django.utils.translation import ugettext_lazy as _

from base_classes.models import BaseMetaData
from faktura.models import Faktura

class FakturaItem(BaseMetaData):
    """ FakturaItem model """

    description = models.CharField(help_text=_('Item Description'), blank=True),
    quantity = models.IntegerField(help_text=_('Quantity'), default=1),
    unit = models.CharField(help_text=_('Kg, Litres, Hours'), blank=True),
    rate = models.IntegerField(help_text=_('Rate or Price per unit'), default=1),
    # amount = models.IntegerField(quantity * rate),

    #Foreign Keys
    faktura_id = models.ForeignKey(Faktura, on_delete=models.CASCADE),
