# Generated by Django 2.1.4 on 2019-01-15 01:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aggregator',
            fields=[
                ('aggregator', models.CharField(max_length=25)),
                ('full_name', models.CharField(default='full_name', max_length=51, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('data', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.FloatField()),
                ('voltage_a', models.FloatField()),
                ('voltage_a_units', models.CharField(default='kWh', max_length=3)),
                ('voltage_b', models.FloatField()),
                ('voltage_b_units', models.CharField(default='kWh', max_length=3)),
                ('voltage_c', models.FloatField()),
                ('voltage_c_units', models.CharField(default='kWh', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('day', models.CharField(max_length=2, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Hour',
            fields=[
                ('hour', models.CharField(max_length=2, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('house', models.CharField(max_length=25)),
                ('full_name', models.CharField(default='full_name', max_length=106, primary_key=True, serialize=False)),
                ('aggregator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash.Aggregator')),
            ],
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('month', models.CharField(max_length=2, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('neighborhood', models.CharField(max_length=25)),
                ('full_name', models.CharField(default='full_name', max_length=78, primary_key=True, serialize=False)),
                ('aggregator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash.Aggregator')),
            ],
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('reading', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('consumption', models.BigIntegerField(default=0)),
                ('consumption_units', models.CharField(default='kWh', max_length=3)),
                ('temperature', models.IntegerField(default=0)),
                ('temperature_units', models.CharField(default='F', max_length=1)),
                ('cost', models.BigIntegerField(default=0)),
                ('currency', models.CharField(default='USD', max_length=3)),
                ('aggregator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash.Aggregator')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash.House')),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash.Neighborhood')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('region', models.CharField(max_length=25)),
                ('full_name', models.CharField(default='full_name', max_length=25, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('year', models.CharField(max_length=4, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='reading',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash.Region'),
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash.Region'),
        ),
        migrations.AddField(
            model_name='house',
            name='neighborhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash.Neighborhood'),
        ),
        migrations.AddField(
            model_name='house',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash.Region'),
        ),
        migrations.AlterUniqueTogether(
            name='data',
            unique_together={('data', 'timestamp', 'voltage_a', 'voltage_a_units', 'voltage_b', 'voltage_b_units', 'voltage_c', 'voltage_c_units')},
        ),
        migrations.AddField(
            model_name='aggregator',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash.Region'),
        ),
        migrations.AlterUniqueTogether(
            name='reading',
            unique_together={('reading', 'date', 'house', 'neighborhood', 'aggregator', 'region', 'consumption', 'temperature', 'cost')},
        ),
        migrations.AlterUniqueTogether(
            name='neighborhood',
            unique_together={('neighborhood', 'aggregator', 'region')},
        ),
        migrations.AlterUniqueTogether(
            name='house',
            unique_together={('house', 'neighborhood', 'aggregator', 'region')},
        ),
        migrations.AlterUniqueTogether(
            name='aggregator',
            unique_together={('aggregator', 'region')},
        ),
    ]
