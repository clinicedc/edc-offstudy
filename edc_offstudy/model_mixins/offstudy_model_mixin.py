from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import options
from django.utils import timezone
from edc_base.model_fields import OtherCharField
from edc_base.model_validators import datetime_not_future
from edc_constants.date_constants import EDC_DATETIME_FORMAT
from edc_identifier.model_mixins import UniqueSubjectIdentifierFieldMixin
from edc_protocol.validators import datetime_not_before_study_start
from edc_visit_schedule.model_mixins import VisitScheduleMethodsModelMixin

options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('consent_model', )


class OffstudyError(Exception):
    pass


class OffstudyModelManager(models.Manager):

    def get_by_natural_key(self, subject_identifier):
        return self.get(subject_identifier=subject_identifier)


class OffstudyModelMixin(UniqueSubjectIdentifierFieldMixin,
                         VisitScheduleMethodsModelMixin, models.Model):
    """Mixin for the Off Study model.
    """

    offstudy_datetime = models.DateTimeField(
        verbose_name="Off-study Date",
        validators=[
            datetime_not_before_study_start,
            datetime_not_future])

    reason = models.CharField(
        verbose_name="Please code the primary reason participant taken off-study",
        max_length=115)

    reason_other = OtherCharField()

    comment = models.TextField(
        max_length=250,
        verbose_name="Comment",
        blank=True,
        null=True)

    objects = OffstudyModelManager()

    def save(self, *args, **kwargs):
        if not self.consented_before_offstudy:
            formatted_date = timezone.localtime(
                self.offstudy_datetime).strftime(EDC_DATETIME_FORMAT)
            raise OffstudyError(
                f'Offstudy date may not be before the date of consent. '
                f'Got {formatted_date}.')
        app_config = django_apps.get_app_config('edc_visit_tracking')
        visit_model_cls = app_config.visit_model_cls(self._meta.app_label)
        app_config = django_apps.get_app_config('edc_appointment')
        appointment_model_cls = django_apps.get_model(app_config.get_configuration(
            related_visit_model=visit_model_cls._meta.label_lower).model)
        self.offstudy_datetime_after_last_visit_or_raise(
            visit_model_cls=visit_model_cls)
        appointment_model_cls.objects.delete_for_subject_after_date(
            self.subject_identifier, self.offstudy_datetime)
        super().save(*args, **kwargs)

    def natural_key(self):
        return (self.subject_identifier, )

    def __str__(self):
        formatted_date = timezone.localtime(
            self.offstudy_datetime).strftime(EDC_DATETIME_FORMAT)
        return f'{self.subject_identifier} {formatted_date}'

    @property
    def consented_before_offstudy(self):
        consent = None
        try:
            model_cls = django_apps.get_model(self._meta.consent_model)
        except AttributeError as e:
            raise OffstudyError(
                f'Failed to lookup consent model. Meta class option '
                f'consent_model={self._meta.consent_model} for model {repr(self)}. '
                f'Got {e}')
        try:
            consent = model_cls.objects.get(
                subject_identifier=self.subject_identifier,
                consent_datetime__lte=self.offstudy_datetime)
        except ObjectDoesNotExist:
            consent = None
        return consent

    def offstudy_datetime_after_last_visit_or_raise(self, visit_model_cls=None):
        last_visit = visit_model_cls.objects.filter(
            subject_identifier=self.subject_identifier).order_by(
                'report_datetime').last()
        if last_visit and (last_visit.report_datetime - self.offstudy_datetime).days > 0:
            formatted_visitdate = timezone.localtime(
                last_visit.report_datetime).strftime(EDC_DATETIME_FORMAT)
            formatted_offstudy = timezone.localtime(
                self.offstudy_datetime).strftime(EDC_DATETIME_FORMAT)
            raise OffstudyError(
                f'Offstudy datetime cannot precede the last visit date of '
                f'{formatted_visitdate}. Got Offstudy date {formatted_offstudy}')

    class Meta:
        abstract = True
        consent_model = None
