# Generated by Django 3.2.5 on 2021-07-18 11:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.CharField(max_length=200, unique=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('father_name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('مرد', 'male'), ('زن', 'female')], default='مرد', max_length=20)),
                ('dob', models.DateField(blank=True, null=True)),
                ('national_cart', models.CharField(choices=[('paper', 'paper'), ('electric', 'electric')], default='electric', max_length=20)),
                ('cart_number', models.CharField(max_length=255)),
                ('page_number', models.IntegerField(blank=True, null=True)),
                ('register_number', models.IntegerField(blank=True, null=True)),
                ('volume', models.IntegerField(blank=True, null=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('cart_image', models.ImageField(default='cart.jpg', upload_to='staff/images')),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('deactive', 'deactive')], default='active', max_length=20)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='staff/images')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StaffJobExp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=200)),
                ('organization', models.CharField(blank=True, max_length=200, null=True)),
                ('salary', models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True)),
                ('duration', models.CharField(blank=True, max_length=200, null=True)),
                ('from_date', models.DateField(blank=True, null=True)),
                ('to_date', models.DateField(blank=True, null=True)),
                ('approve_letter', models.ImageField(blank=True, null=True, upload_to='staff/job/images')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.staff')),
            ],
        ),
        migrations.CreateModel(
            name='StaffEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edu_title', models.CharField(max_length=200)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('diploma', models.ImageField(blank=True, null=True, upload_to='staff/edu/images')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.staff')),
            ],
        ),
    ]
