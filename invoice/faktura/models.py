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
    faktura_id = models.ForeignKey(Faktura),

class Faktura (BaseMetadata):
    """ invoice / faktura model"""

    # TO-DO user_id (FK)
    invoice_number = models.IntegerField(primary_key=True),    # TO-DO (counter) company_id + invoice_number → unique
    description = models.CharField(help_text=_('Item Description'), blank=True),
    # TO-DO ? language (for backend, maybe should be a setting company or user wide)
    currency = unit = models.CharField(help_text=_('Currency')),
    # TO-DO registered_address (main) ← address of user’s company
    # TO-DO billing_account (main) ← account of user’s company
    # TO-DO recipient (FK to Customer)
    due_date = models.DateTimeField(help_text=_('Last day for pay'))
    # TO-DO footer (from company invoice_footer)

    # Fields for the Recurring feature
    recurring = models.BooleanField(help_text=_('Turn on to send a copy of the invoice again'),
                                    default=False)
    recurring_issue_start_date = models.DateField(help_text=_('Date to start sending the invoice')),
    recurring_day = models.DateField(help_text=_('Date for the next automatic invoice to be sent')),
    # TO-DO recurring_next_issue_date → to be calculated by a celery job every n hours.

    INTERVAL = (
        (0, _('Daily')),
        (1, _('Weekly')),
        (2, _('Bi-Weekly')),
        (3, _('Monthly')),
        (4, _('Yearly')),
    )
    recurring_interval = models.IntegerField(choices=INTERVAL, default=3)

    # Faktura STATUSES
    STATUSES = (
        (0, _('Open')),
        (1, _('Overdue')),
        (2, _('Paid')),
        (3, _('Cancelled')),
        (4, _('Questioned')),
        (5, _('Draft')),
    )
    status = models.IntegerField(help_text=_('Status of the invoice')choices=STATUSES, default=0)

    # Functions for calculate the totals
    # TO-DO amount_pre_tax to be calculated based upon invoiceitem/s)
    # TO-DO amount_final (to be calculated based upon invoiceitem/s)
