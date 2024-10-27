# Generated by Django 4.2.6 on 2024-10-27 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organisations', '0001_initial'),
        ('socials', '0001_initial'),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='org_admins',
            field=models.ManyToManyField(blank=True, related_name='org_admins', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='organisation',
            name='org_category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.orgcategory'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='org_directions',
            field=models.ManyToManyField(blank=True, to='catalog.orgdirection'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='org_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='org_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='organisation',
            name='org_socials',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='organisation', to='socials.orgsocials'),
        ),
    ]
