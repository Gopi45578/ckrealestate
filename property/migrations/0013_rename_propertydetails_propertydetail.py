# Generated by Django 4.2 on 2023-05-11 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "property",
            "0012_propertyavailability_property_search_date_searched_and_more",
        ),
    ]

    operations = [
        migrations.RenameModel(
            old_name="PropertyDetails",
            new_name="PropertyDetail",
        ),
    ]
