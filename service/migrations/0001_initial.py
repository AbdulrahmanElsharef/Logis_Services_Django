# Generated by Django 3.2 on 2023-02-20 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_us', models.TextField(max_length=5000)),
                ('image', models.ImageField(upload_to='about_us')),
            ],
        ),
        migrations.CreateModel(
            name='FaqAsked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ask', models.CharField(max_length=200)),
                ('answer', models.TextField(verbose_name=1000)),
            ],
        ),
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('job', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='OurTeam')),
                ('job_info', models.TextField(max_length=300)),
                ('facebook', models.CharField(max_length=150)),
                ('instagram', models.CharField(max_length=150)),
                ('linkedin', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plane_name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.TextField(max_length=500)),
                ('description', models.TextField(max_length=10000)),
                ('ser_image', models.ImageField(upload_to='Service')),
                ('det_image', models.ImageField(blank=True, null=True, upload_to='Service')),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
                ('review', models.TextField(max_length=1000)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Service_Review', to='service.service')),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offers', models.CharField(max_length=200)),
                ('plane_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Pricing_Offer', to='service.pricing')),
            ],
        ),
        migrations.CreateModel(
            name='LastService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.TextField(max_length=300)),
                ('description', models.TextField(max_length=5000)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Last_Service', to='service.service')),
            ],
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conditione', models.TextField(max_length=500)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_Condition', to='service.service')),
            ],
        ),
    ]
