# Generated by Django 4.1.7 on 2023-04-02 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_users_last_updated_alter_users_publish_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Publish')], default='d', max_length=10),
        ),
    ]
