# Generated by Django 3.2.5 on 2021-07-22 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fmapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='update',
            field=models.DateTimeField(null=True, verbose_name='최종수정일'),
        ),
        migrations.AlterField(
            model_name='community',
            name='body',
            field=models.TextField(verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='community',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name='작성일'),
        ),
        migrations.AlterField(
            model_name='community',
            name='title',
            field=models.CharField(max_length=200, verbose_name='제목'),
        ),
        migrations.AlterField(
            model_name='community',
            name='writer',
            field=models.CharField(max_length=100, verbose_name='작성자'),
        ),
    ]