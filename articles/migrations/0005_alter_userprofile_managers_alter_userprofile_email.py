# Generated by Django 5.2 on 2025-05-17 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_article_options_alter_article_content_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=225, unique=True, verbose_name='email adress'),
        ),
    ]
