# Generated by Django 3.2.6 on 2021-08-12 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_user_users'),
        ('qna', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='qna',
            options={'verbose_name': '게시판', 'verbose_name_plural': '게시판'},
        ),
        migrations.AlterField(
            model_name='qna',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.users', verbose_name='작성자'),
        ),
        migrations.AlterModelTable(
            name='qna',
            table='board3',
        ),
    ]
