# Generated by Django 3.2.19 on 2023-05-21 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.CharField(editable=False, max_length=32)),
                ('event_lead', models.CharField(max_length=50)),
                ('contact_email', models.EmailField(max_length=254)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=400)),
                ('date', models.DateTimeField()),
                ('time', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendee_number', models.CharField(editable=False, max_length=32)),
                ('attendee_name', models.CharField(max_length=50)),
                ('attendee_email', models.EmailField(max_length=254)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.event')),
            ],
        ),
    ]
