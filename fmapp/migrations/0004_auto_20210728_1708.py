# Generated by Django 3.2.5 on 2021-07-28 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fmapp', '0003_auto_20210728_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComHospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='제목')),
                ('body', models.TextField(verbose_name='내용')),
                ('writer', models.CharField(max_length=200, verbose_name='작성자')),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='작성일')),
                ('update', models.DateTimeField(auto_now=True, null=True, verbose_name='최종수정일')),
            ],
        ),
        migrations.CreateModel(
            name='Qna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='제목')),
                ('body', models.TextField(verbose_name='내용')),
                ('writer', models.CharField(max_length=200, verbose_name='작성자')),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='작성일')),
                ('update', models.DateTimeField(auto_now=True, null=True, verbose_name='최종수정일')),
            ],
        ),
        migrations.AlterField(
            model_name='community',
            name='writer',
            field=models.CharField(max_length=200, verbose_name='작성자'),
        ),
    ]