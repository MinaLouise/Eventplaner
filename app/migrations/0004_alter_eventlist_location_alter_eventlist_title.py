# Generated by Django 4.2.7 on 2023-12-04 02:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_alter_eventlist_location_alter_eventlist_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eventlist",
            name="location",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="eventlist",
            name="title",
            field=models.TextField(),
        ),
    ]
