# Generated by Django 3.1.5 on 2021-09-16 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('c360app', '0005_auto_20210916_1035'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField()),
                ('photo', models.ImageField(default='c360app/facerec/detected/noimg.png', upload_to='detected/')),
                ('emp_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='c360app.employee')),
            ],
        ),
    ]