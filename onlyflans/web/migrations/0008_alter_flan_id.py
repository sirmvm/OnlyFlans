# Generated by Django 3.2.4 on 2022-03-30 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_remove_flan_deseo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flan',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]