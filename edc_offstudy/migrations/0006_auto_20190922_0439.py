# Generated by Django 2.2.2 on 2019-09-22 02:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("edc_offstudy", "0005_auto_20190305_0123")]

    operations = [
        migrations.AlterField(
            model_name="historicalsubjectoffstudy",
            name="subject_identifier",
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="subjectoffstudy",
            name="subject_identifier",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
