[![Build Status](https://travis-ci.org/botswana-harvard/edc-offstudy.svg?branch=develop)](https://travis-ci.org/botswana-harvard/edc-offstudy)
[![Coverage Status](https://coveralls.io/repos/botswana-harvard/edc-offstudy/badge.svg)](https://coveralls.io/r/botswana-harvard/edc-offstudy)

# edc-offstudy

Base classes for off study process

See tests for more complete examples.

###Note:
edc_offstudy requires modules from `edc` and is only tested on PY2 Django 1.6

###Usage
Declare an off study model:

	class MyOffStudyModel(CrfModelMixin, OffStudyModelMixin, BaseUuidModel):
	
	    my_visit = models.OneToOneField(MyVisit)
	
	    class Meta:
	        app_label = 'my_app'


Declare your visit model and tell it what the off_study_model is:

    class MyVisit(OffStudyMixin, MetaDataMixin, PreviousVisitMixin, BaseVisitTracking):

        off_study_model = ('my_app', 'TestOffStudyModel')

        REQUIRES_PREVIOUS_VISIT = True

        def get_subject_identifier(self):
            return self.appointment.registered_subject.subject_identifier

        def custom_post_update_entry_meta_data(self):
            pass

        class Meta:
            app_label = 'my_app'

Declare your scheduled models

    class ScheduledCrfOne(CrfModelMixin, OffStudyMixin, MetaDataMixin, BaseUuidModel):

        off_study_model = ('my_app', 'MyOffStudyModel')
    
        q1 = models.CharField()
        q2 = models.CharField()
        q3 = models.CharField()

        class Meta:
            app_label = 'my_app'
    
