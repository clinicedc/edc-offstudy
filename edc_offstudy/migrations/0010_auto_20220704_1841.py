# Generated by Django 3.2.13 on 2022-07-04 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("edc_offstudy", "0009_auto_20200513_0023"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="historicalsubjectoffstudy",
            options={
                "get_latest_by": ("history_date", "history_id"),
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical subject offstudy",
                "verbose_name_plural": "historical subject offstudys",
            },
        ),
        migrations.AlterField(
            model_name="historicalsubjectoffstudy",
            name="history_date",
            field=models.DateTimeField(db_index=True),
        ),
    ]
