# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('pobox', models.CharField(max_length=256)),
                ('ext', models.CharField(max_length=256)),
                ('street', models.CharField(max_length=256)),
                ('locality', models.CharField(max_length=256)),
                ('region', models.CharField(max_length=256)),
                ('code', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=256)),
                ('geo', models.CharField(max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('n', models.CharField(max_length=1024)),
                ('nickname', models.CharField(max_length=128)),
                ('bday', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('N', 'None'), ('U', 'Unknow')], max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('mail_type', models.CharField(choices=[('home', 'Home'), ('work', 'Work'), ('other', 'Other')], max_length=10)),
                ('uri', models.CharField(max_length=255)),
                ('contact', models.ForeignKey(to='keeper.Contact')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('tel_type', models.CharField(choices=[('home', 'Home'), ('work', 'Work'), ('mobile', 'Mobile'), ('main', 'main'), ('home fax', 'Home Fax'), ('work fax', 'Work Fax'), ('pager', 'Pager'), ('other', 'other')], max_length=10)),
                ('uri', models.CharField(max_length=255)),
                ('contact', models.ForeignKey(to='keeper.Contact')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('url_type', models.CharField(choices=[('homepage', 'Homepage'), ('home', 'Home'), ('work', 'work'), ('other', 'Other')], max_length=10)),
                ('uri', models.CharField(max_length=255)),
                ('contact', models.ForeignKey(to='keeper.Contact')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='address',
            name='contact',
            field=models.ForeignKey(to='keeper.Contact'),
            preserve_default=True,
        ),
    ]
