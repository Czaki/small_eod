# Generated by Django 3.1.1 on 2020-10-01 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0014_remove_letter_ordering'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documenttype',
            name='name',
            field=models.CharField(help_text='Type of letter', max_length=256, unique=True, verbose_name='Document type'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='comment',
            field=models.TextField(blank=True, help_text='Comment for letter.', verbose_name='Comment'),
        ),
    ]
