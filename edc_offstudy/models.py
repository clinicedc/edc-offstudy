from edc_action_item.models import ActionNoManagersModelMixin
from edc_consent.model_mixins import RequiresConsentFieldsModelMixin
from edc_identifier.managers import SubjectIdentifierManager
from edc_model.models import BaseUuidModel, HistoricalRecords
from edc_sites.models import CurrentSiteManager, SiteModelMixin

from .constants import END_OF_STUDY_ACTION
from .model_mixins import OffstudyModelMixin


class SubjectOffstudy(
    RequiresConsentFieldsModelMixin,
    OffstudyModelMixin,
    SiteModelMixin,
    ActionNoManagersModelMixin,
    BaseUuidModel,
):
    action_name = END_OF_STUDY_ACTION

    objects = SubjectIdentifierManager()

    on_site = CurrentSiteManager()

    history = HistoricalRecords()

    class Meta(BaseUuidModel.Meta):
        verbose_name = "Subject Offstudy"
        verbose_name_plural = "Subject Offstudy"
        indexes = ActionNoManagersModelMixin.Meta.indexes + BaseUuidModel.Meta.indexes
