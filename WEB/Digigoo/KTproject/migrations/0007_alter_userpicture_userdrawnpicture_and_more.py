# Generated by Django 4.0 on 2021-12-29 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KTproject', '0006_alter_userpicture_userdrawnpicture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpicture',
            name='UserDrawnPicture',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='userpicture',
            name='contents',
            field=models.TextField(blank=True, null=True),
        ),
    ]
