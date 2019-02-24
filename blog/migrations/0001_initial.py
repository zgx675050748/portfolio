# Generated by Django 2.1.7 on 2019-02-24 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='文章标题', max_length=50)),
                ('date', models.DateField()),
                ('image', models.ImageField(default='default.png', upload_to='')),
                ('text', models.CharField(default='正文', max_length=100)),
            ],
        ),
    ]