# Generated by Django 4.2.7 on 2024-02-04 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Declined', 'Declined'), ('Pending', 'Pending')], max_length=20)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
