from django.db import models

from ..utils import raise_if_offstudy


class OffstudyCrfModelMixin(models.Model):

    """Model mixin for CRF models.

    A mixin for CRF models to add the ability to determine
    if the subject is off study as of this CRFs report_datetime.

    CRFs by definition include CrfModelMixin in their declaration.
    See edc_visit_tracking.

    Also requires field "report_datetime"
    """

    def save(self, *args, **kwargs):
        self.raise_if_offstudy()
        super().save(*args, **kwargs)

    def raise_if_offstudy(self):
        raise_if_offstudy(
            source_obj=self,
            subject_identifier=self.related_visit.subject_identifier,
            report_datetime=self.report_datetime,
            visit_schedule_name=self.related_visit.visit_schedule_name,
        )

    class Meta:
        abstract = True
