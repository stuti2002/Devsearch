# Generated by Django 3.2.6 on 2021-12-13 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_project_upload_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='Upload_image',
            field=models.ImageField(blank='True', default='Google.png', null='True', upload_to='static/images/'),
        ),
    ]
