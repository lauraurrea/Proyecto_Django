# Generated by Django 4.1.5 on 2023-04-10 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amigos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('follow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amigo_de', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amigos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'follow')},
            },
        ),
    ]
