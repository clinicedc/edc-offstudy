[![Build Status](https://travis-ci.org/botswana-harvard/edc-offstudy.svg?branch=develop)](https://travis-ci.org/botswana-harvard/edc-offstudy)
[![Coverage Status](https://coveralls.io/repos/botswana-harvard/edc-offstudy/badge.svg)](https://coveralls.io/r/botswana-harvard/edc-offstudy)

# edc-offstudy

Base classes for off study process

See tests for more complete examples.

###Note:
edc_offstudy requires modules from `edc` and is only tested on PY2 Django 1.6

###Usage
Declare an off study model and tell it what the visit model is:

    class TestOffStudyModel(OffStudyModelMixin, BaseUuidModel):

        VISIT_MODEL = TestVisitModel

        registered_subject = models.OneToOneField(RegisteredSubject)

        class Meta:
          app_label = 'my_app'


Declare your visit model and tell it what the OFF_STUDY_MODEL is:

    class TestVisitModel(OffStudyMixin, MetaDataMixin, PreviousVisitMixin, BaseVisitTracking):

        OFF_STUDY_MODEL = ('edc_offstudy', 'TestOffStudyModel')

        REQUIRES_PREVIOUS_VISIT = True

        def get_subject_identifier(self):
            return self.appointment.registered_subject.subject_identifier

        def custom_post_update_entry_meta_data(self):
            pass

        class Meta:
            app_label = 'my_app'

Declare your scheduled models

    class ScheduledCrfOne(OffStudyMixin, MetaDataMixin, BaseUuidModel):

        OFF_STUDY_MODEL = ('edc_offstudy', 'TestOffStudyModel')
    
        q1 = models.CharField()
        q2 = models.CharField()
        q3 = models.CharField()

        class Meta:
            app_label = 'my_app'
    
