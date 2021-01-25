# Generated by Django 3.0.4 on 2020-05-12 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("edc_offstudy", "0008_auto_20191102_0033"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="subjectoffstudy",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "get_latest_by": "modified",
                "ordering": ("-modified", "-created"),
            },
        ),
    ]