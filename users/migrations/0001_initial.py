# Generated by Django 3.2.5 on 2021-07-13 13:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=250, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('birth_date', models.DateTimeField(blank=True, null=True)),
                ('local', models.BooleanField(default='False')),
                ('city', models.CharField(blank=True, choices=[('AMMAN', 'Amman'), ('ZARQA', 'Zarqa'), ('IRBID', 'Irbid'), ('MAFRAQ', 'Mafraq'), ('SALT', 'Salt'), ('MADABA', 'Madaba'), ('AQABA', 'Aqaba'), ('MA`AN', 'Ma`an'), ('JARASH', 'Jarash'), ('AJLUN', 'Ajlun'), ('KARAK', 'Karak'), ('TAFILAH', 'Tafilah')], max_length=255, null=True)),
                ('member', models.CharField(blank=True, choices=[('EDUCATOR', 'educator'), ('ORGANIZATION', 'organization'), ('STUDENT', 'student')], max_length=255, null=True)),
                ('organization_name', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=10, null=True)),
                ('specialization', models.CharField(blank=True, max_length=255, null=True)),
                ('interests', models.TextField(blank=True, null=True)),
                ('biography', models.TextField(blank=True, null=True)),
                ('current_organization', models.CharField(blank=True, max_length=255, null=True)),
                ('organization_summary', models.TextField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('freelancer', models.BooleanField(default=False)),
                ('hourly_tutoring_rate', models.IntegerField(blank=True, null=True)),
                ('services', models.TextField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
