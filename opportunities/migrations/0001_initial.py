# Generated by Django 3.1.3 on 2020-11-06 15:29

import bsct.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=95, unique=True)),
                ('address', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
            bases=(models.Model, bsct.models.BSCTModelMixin),
        ),
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=95)),
                ('amount', models.FloatField()),
                ('stage', models.CharField(choices=[('DISCOVERY', 'DISCOVERY'), ('PROPOSAL_SHARED', 'PROPOSAL_SHARED'), ('NEGOTIATIONS', 'NEGOTIATIONS')], max_length=58)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='opportunities', to='opportunities.account', to_field='username')),
            ],
            bases=(models.Model, bsct.models.BSCTModelMixin),
        ),
    ]
