# Generated by Django 3.0.1 on 2020-01-09 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tagnamespace',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tagnamespace_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tagnamespace',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tagnamespace_modified_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
