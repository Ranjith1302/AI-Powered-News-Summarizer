# Generated by Django 4.2.16 on 2025-02-18 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_newsarticle_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsarticle',
            options={'ordering': ['-published_at']},
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='description',
            field=models.TextField(),
        ),
    ]
