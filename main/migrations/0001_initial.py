# Generated by Django 2.2.7 on 2023-06-19 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=128, null=True, unique=True, verbose_name='项目编号')),
                ('country', models.CharField(choices=[('1', '国内'), ('2', '国外')], max_length=1, verbose_name='国家')),
                ('country_name', models.CharField(max_length=128, null=True, unique=True, verbose_name='国家名称')),
                ('platform', models.CharField(choices=[('1', 'AMD'), ('2', 'ACA'), ('3', 'AIN'), ('4', 'BCA'), ('5', 'ALP'), ('6', 'APN')], max_length=1, verbose_name='国家名称')),
                ('introduction', models.CharField(max_length=128, null=True, unique=True, verbose_name='项目简介')),
                ('price', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='价格')),
                ('duration', models.IntegerField(verbose_name='时长')),
                ('date', models.DateTimeField(verbose_name='时间')),
            ],
            options={
                'db_table': 'survey_message',
            },
        ),
    ]
