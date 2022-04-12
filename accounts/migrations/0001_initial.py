# Generated by Django 4.0.3 on 2022-04-12 06:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('image', models.ImageField(null=True, upload_to='')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('JobTitle', models.CharField(max_length=132, null=True)),
                ('position', models.CharField(max_length=132, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
