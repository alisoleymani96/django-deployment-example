# Generated by Django 2.2.2 on 2020-02-13 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessrecord',
            name='name',
            field=models.ForeignKey(on_delete='CASCADE', to='first_app.WebPage'),
        ),
    ]
