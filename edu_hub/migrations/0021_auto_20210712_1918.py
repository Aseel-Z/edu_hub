# Generated by Django 3.2.5 on 2021-07-12 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu_hub', '0020_alter_member_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='created_at',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='member',
            name='updated_at',
            field=models.DateField(),
        ),
    ]
