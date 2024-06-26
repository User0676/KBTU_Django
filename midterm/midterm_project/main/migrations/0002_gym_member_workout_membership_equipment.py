# Generated by Django 4.2.11 on 2024-03-11 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('gym_id', models.AutoField(primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=100)),
                ('instructor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.instructor')),
            ],
            options={
                'db_table': 'gym',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('membership_type', models.CharField(max_length=50)),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='main.instructor')),
            ],
            options={
                'db_table': 'member',
            },
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('workout_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workouts', to='main.gym')),
            ],
            options={
                'db_table': 'workout',
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('membership_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='main.member')),
            ],
            options={
                'db_table': 'membership',
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('equipment_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipment', to='main.gym')),
            ],
            options={
                'db_table': 'equipment',
            },
        ),
    ]
