# Generated by Django 5.0.4 on 2024-04-29 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unique_app', '0003_category_post_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('project_type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('file', models.FileField(blank=True, null=True, upload_to='inquiries/')),
            ],
        ),
    ]
