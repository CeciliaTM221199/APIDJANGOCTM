# Generated by Django 3.2.4 on 2023-11-07 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_registrou_id_registrou'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrou',
            name='id_registroU',
            field=models.AutoField(db_column='id_registro', primary_key=True, serialize=False),
        ),
    ]