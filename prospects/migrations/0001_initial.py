# Generated by Django 3.2.19 on 2023-06-26 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='business_prospect',
            fields=[
                ('lead_id', models.AutoField(primary_key=True, serialize=False)),
                ('facility_name', models.CharField(max_length=300)),
                ('county', models.CharField(max_length=30)),
                ('town', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact_person', models.CharField(blank=True, max_length=200, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=20, null=True)),
                ('comment', models.TextField(blank=True)),
                ('created_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField(blank=True)),
                ('feedback_timestamp', models.DateTimeField(auto_now_add=True)),
                ('prospect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prospects.business_prospect')),
            ],
        ),
        migrations.CreateModel(
            name='conversion_tracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demostatus', models.CharField(choices=[('DONE', 'DONE'), ('PENDING', 'PENDING')], default='PENDING', max_length=30)),
                ('demodate', models.DateField(blank=True, default=None, null=True)),
                ('Attendees', models.TextField(blank=True)),
                ('meeting', models.CharField(blank=True, choices=[('PHYSICAL', 'PHYSICAL'), ('VIRTUAL', 'VIRTUAL')], max_length=30)),
                ('feedback', models.TextField(blank=True)),
                ('assessmentdate', models.DateField(blank=True, default=None, null=True)),
                ('report', models.FileField(blank=True, upload_to='documents/')),
                ('reportdate', models.DateField(blank=True, default=None, null=True)),
                ('expression', models.FileField(blank=True, upload_to='documents/')),
                ('facility_license', models.FileField(blank=True, upload_to='documents/')),
                ('krapin', models.FileField(blank=True, upload_to='documents/')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('demo_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prospects.business_prospect')),
            ],
        ),
    ]