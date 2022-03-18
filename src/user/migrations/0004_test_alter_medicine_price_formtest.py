# Generated by Django 4.0.3 on 2022-03-18 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_user_form_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('test_id', models.AutoField(primary_key=True, serialize=False)),
                ('test_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='medicine',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.CreateModel(
            name='FormTest',
            fields=[
                ('ft_id', models.AutoField(primary_key=True, serialize=False)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=7)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.form')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.test')),
            ],
        ),
    ]