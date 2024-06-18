# Generated by Django 5.0.1 on 2024-04-02 19:11

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comp_Reg',
            fields=[
                ('c_id', models.CharField(default=1, max_length=100, primary_key=True, serialize=False)),
                ('c_pic', models.FileField(default='', upload_to='Dailychores_Security/Companies/')),
                ('c_pass', models.CharField(max_length=32)),
                ('c_name', models.CharField(max_length=50)),
                ('c_ceo', models.CharField(max_length=50)),
                ('c_phone', models.CharField(max_length=13)),
                ('c_email', models.EmailField(max_length=30)),
                ('c_city', models.CharField(max_length=20)),
                ('c_regno', models.CharField(max_length=30)),
                ('c_addr', models.TextField()),
                ('c_about', models.TextField()),
                ('time', models.TimeField(default=django.utils.timezone.now)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=13)),
                ('question', models.TextField()),
                ('time', models.TimeField(default=django.utils.timezone.now)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_name', models.CharField(default=1, max_length=50, primary_key=True, serialize=False, unique=True)),
                ('event_venue', models.CharField(default='Auditorium', max_length=50)),
                ('event_date', models.DateField(default=django.utils.timezone.now)),
                ('event_description', models.TextField()),
                ('event_pic', models.FileField(default='', upload_to='Dailychores_Security/common_images/')),
            ],
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('remark', models.TextField()),
                ('rating', models.CharField(default=1, max_length=10)),
                ('time', models.TimeField(default=django.utils.timezone.now)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='User_Reg',
            fields=[
                ('u_name', models.CharField(max_length=50)),
                ('u_pic', models.FileField(default='', upload_to='Dailychores_Security/Users/')),
                ('u_email', models.EmailField(max_length=50)),
                ('u_phone', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('u_pass', models.CharField(max_length=32)),
                ('u_city', models.CharField(max_length=50)),
                ('u_addr', models.TextField()),
                ('time', models.TimeField(default=django.utils.timezone.now)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_category', models.CharField(max_length=50)),
                ('emp_category_pic', models.FileField(default='', upload_to='Dailychores_Security/Employee_categories/')),
                ('emp_description', models.CharField(max_length=100)),
                ('comp_reg', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dcs_app.comp_reg')),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Reg',
            fields=[
                ('emp_id', models.CharField(max_length=50)),
                ('emp_pic', models.FileField(default='', upload_to='Dailychores_Security/Employees/')),
                ('emp_name', models.CharField(max_length=50)),
                ('emp_phone', models.CharField(default=1, max_length=13, primary_key=True, serialize=False)),
                ('emp_status', models.CharField(default='Available', max_length=13)),
                ('emp_city', models.CharField(max_length=50)),
                ('emp_addr', models.TextField()),
                ('time', models.TimeField(default=django.utils.timezone.now)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('emp_reg', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dcs_app.employee_category')),
            ],
        ),
        migrations.CreateModel(
            name='Hiring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=50)),
                ('job_description', models.TextField()),
                ('job_requirement', models.CharField(max_length=50)),
                ('job_location', models.CharField(max_length=50)),
                ('job_salary', models.CharField(max_length=50)),
                ('job_age_limit', models.CharField(max_length=5)),
                ('job_mail', models.CharField(max_length=50)),
                ('job_lastdate_toapply', models.DateField(default=django.utils.timezone.now)),
                ('job_gender', models.CharField(max_length=10)),
                ('job_seats', models.CharField(max_length=5)),
                ('job_post_link', models.CharField(max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dcs_app.comp_reg')),
            ],
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('js_pic', models.FileField(default='', upload_to='Dailychores_Security/Job_seekers/')),
                ('js_name', models.CharField(max_length=50)),
                ('js_age', models.CharField(max_length=10)),
                ('js_gender', models.CharField(max_length=10)),
                ('js_address', models.TextField()),
                ('js_phone', models.CharField(max_length=15)),
                ('js_details', models.CharField(max_length=50)),
                ('hiring', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dcs_app.hiring')),
            ],
        ),
    ]
