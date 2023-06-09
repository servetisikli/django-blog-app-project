# Generated by Django 4.1.7 on 2023-04-02 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_users_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Publish')], max_length=10),
        ),
    ]
