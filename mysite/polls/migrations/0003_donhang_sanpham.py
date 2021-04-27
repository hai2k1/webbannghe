# Generated by Django 3.1.5 on 2021-04-26 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20210426_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='donhang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hoadon', models.CharField(max_length=999999, verbose_name='hóa đơn')),
                ('sanpham', models.CharField(max_length=99999, verbose_name='sản phẩm khách đặt')),
                ('tien', models.CharField(max_length=999999, verbose_name='giá bán')),
                ('ngay', models.DateField(auto_now_add=True, verbose_name='ngày khách đặt')),
            ],
        ),
        migrations.CreateModel(
            name='sanpham',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tensanpham', models.CharField(max_length=50, verbose_name='Tên sản phẩm')),
                ('giaban', models.CharField(max_length=50, verbose_name='giá sản phẩm')),
            ],
        ),
    ]