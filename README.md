[![Build Status](https://travis-ci.com/clinicedc/edc-offstudy.svg?branch=develop)](https://travis-ci.com/clinicedc/edc-offstudy)
[![Coverage Status](https://coveralls.io/repos/clinicedc/edc-offstudy/badge.svg)](https://coveralls.io/r/clinicedc/edc-offstudy)

# edc-offstudy

Base classes for off study process

See tests for more complete examples.

The offstudy model is linked to scheduled models by the visit schedule.

    # visit_schedule.py
    ...
    visit_schedule1 = VisitSchedule(
        name='visit_schedule1',
        offstudy_model='edc_appointment.subjectoffstudy',
        ...)
    ...


Declare the offstudy model referenced in the visit schedule using the `OffstudyModelMixin`:

    class SubjectOffstudy(OffstudyModelMixin, BaseUuidModel):
        
         pass

When the offstudy model is saved, the data is validated relative to the consent and visit model. An offstudy datetime should make sense relative to these models.

Unused appointments in the future relative to the offstudy datetime will be removed.

> Note: There is some redundancy with this model and the offschedule model from `edc-visit-schedule`. This needs to be resolved.
