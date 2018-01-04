from django.db import models
from django.utils.translation import ugettext_lazy as _

from base_classes.models import BaseMetaData


class Faktura(BaseMetaData):
    """ invoice / faktura model"""

    # TO-DO user_id (FK)
    invoice_number = models.IntegerField(primary_key=True)  # TO-DO (counter) company_id + invoice_number → unique

    # Faktura STATUSES
    STATUSES = (
        (0, _('Open')),
        (1, _('Overdue')),
        (2, _('Paid')),
        (3, _('Cancelled')),
        (4, _('Questioned')),
    )
    status = models.IntegerField(help_text=_('Status of the invoice'), choices=STATUSES, default=0)

    description = models.CharField(help_text=_('Item Description'), max_length=512, blank=True)
    # TO-DO ? language (for backend, maybe should be a setting company or user wide)
    currency = models.CharField(help_text=_('$, £, etc'), max_length=16)
    # TO-DO registered_address (main) ← address of user’s company
    # TO-DO billing_account (main) ← account of user’s company
    # TO-DO recipient (FK to Customer)
    due_date = models.DateField(help_text=_('Last day to pay'))
    # TO-DO footer (from company invoice_footer)

    # Fields for the Recurring feature
    recurring = models.BooleanField(help_text=_('Turn on to send a copy of the invoice again'), default=False)

    INTERVAL = (
        (0, _('Daily')),
        (1, _('Weekly')),
        (2, _('Bi-Weekly')),
        (3, _('Monthly')),
        (4, _('Yearly')),
    )
    recurring_interval = models.IntegerField(choices=INTERVAL, default=3, blank=True)

    recurring_issue_start_date = models.DateField(help_text=_('Date to start sending the invoice'), blank=True)
    recurring_day = models.DateField(help_text=_('Date for the next automatic invoice to be sent'), blank=True)    # TO-DO  → to be calculated by a celery job every n hours.

    # Functions for calculate the totals
    # TO-DO amount_pre_tax to be calculated based upon invoiceitem/s), tax could be a field in company or here.
    # TO-DO amount_final (to be calculated based upon invoiceitem/s)

    @property
    def amount_total(self):
        return self.quantity * self.rate

    def __str__(self):
        """Returns the invoice number if called alone"""
        return "%s" % (self.invoice_number)
