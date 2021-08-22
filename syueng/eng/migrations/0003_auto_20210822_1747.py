# Generated by Django 3.2.6 on 2021-08-22 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('division', '0003_auto_20210818_2354'),
        ('eng', '0002_alter_post_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('desc', models.CharField(max_length=512)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='division.team')),
            ],
        ),
    ]