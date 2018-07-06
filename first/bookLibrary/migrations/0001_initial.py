# Generated by Django 2.0.7 on 2018-07-06 16:33

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_created=True, help_text='创建时间')),
                ('modify_date', models.DateTimeField(auto_now_add=True, help_text='创建时间')),
                ('is_delete', models.BooleanField(default=False, help_text='是否删除，默认为否')),
                ('is_discard', models.BooleanField(default=False, help_text='是否废弃，默认为否')),
                ('order', models.IntegerField(default=99, help_text='排序')),
                ('name', models.CharField(default='', help_text='作者名字', max_length=32)),
                ('age', models.IntegerField(default=0, help_text='作者年龄')),
                ('sex', models.CharField(default='女', help_text='性别', max_length=16)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('notDeleteManager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_created=True, help_text='创建时间')),
                ('modify_date', models.DateTimeField(auto_now_add=True, help_text='创建时间')),
                ('is_delete', models.BooleanField(default=False, help_text='是否删除，默认为否')),
                ('is_discard', models.BooleanField(default=False, help_text='是否废弃，默认为否')),
                ('order', models.IntegerField(default=99, help_text='排序')),
                ('name', models.CharField(default='', help_text='书名', max_length=64)),
                ('publish_date', models.CharField(default='', help_text='出版日期', max_length=64)),
                ('author', models.ForeignKey(help_text='作者', null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookLibrary.Author')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('notDeleteManager', django.db.models.manager.Manager()),
            ],
        ),
    ]
