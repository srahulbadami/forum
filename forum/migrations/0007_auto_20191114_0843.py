# Generated by Django 2.2.7 on 2019-11-14 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_comment_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='asd', max_length=80),
            preserve_default=False,
        ),
    ]
