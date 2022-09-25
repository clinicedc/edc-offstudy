# Generated by Django 3.2.13 on 2022-09-24 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("edc_action_item", "0031_auto_20220922_2236"),
        ("edc_offstudy", "0014_auto_20220918_0508"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalsubjectoffstudy",
            name="action_identifier",
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="historicalsubjectoffstudy",
            name="action_item",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AddField(
            model_name="historicalsubjectoffstudy",
            name="action_item_reason",
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name="historicalsubjectoffstudy",
            name="parent_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="historicalsubjectoffstudy",
            name="parent_action_item",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AddField(
            model_name="historicalsubjectoffstudy",
            name="related_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="historicalsubjectoffstudy",
            name="related_action_item",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AddField(
            model_name="subjectoffstudy",
            name="action_identifier",
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="subjectoffstudy",
            name="action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AddField(
            model_name="subjectoffstudy",
            name="action_item_reason",
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name="subjectoffstudy",
            name="parent_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="subjectoffstudy",
            name="parent_action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AddField(
            model_name="subjectoffstudy",
            name="related_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="subjectoffstudy",
            name="related_action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="edc_action_item.actionitem",
            ),
        ),
    ]