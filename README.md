[![Build Status](https://travis-ci.org/clinicedc/edc-offstudy.svg?branch=develop)](https://travis-ci.org/clinicedc/edc-offstudy)
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


