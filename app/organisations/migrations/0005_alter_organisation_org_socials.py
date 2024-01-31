# Generated by Django 4.2.6 on 2024-02-01 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("socials", "0002_alter_orgsocials_facebook_alter_orgsocials_imo_and_more"),
        ("organisations", "0004_alter_organisation_org_working_hours"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organisation",
            name="org_socials",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="socials.orgsocials",
            ),
        ),
    ]
