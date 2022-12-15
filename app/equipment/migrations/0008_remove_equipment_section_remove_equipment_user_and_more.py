# Generated by Django 4.1.4 on 2022-12-15 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("equipment", "0007_alter_equipment_floor"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="equipment",
            name="section",
        ),
        migrations.RemoveField(
            model_name="equipment",
            name="user",
        ),
        migrations.AddField(
            model_name="equipment",
            name="user_section",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="equipment",
            name="floor",
            field=models.CharField(
                choices=[
                    ("Ground", "Ground"),
                    ("First", "1st"),
                    ("Second", "2nd"),
                    ("Third", "3rd"),
                ],
                max_length=100,
            ),
        ),
    ]