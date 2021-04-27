from django.db import models

# Create your models here.
class sanpham(models.Model):
    tensanpham = models.CharField(("Tên sản phẩm"), max_length=50)
    giaban = models.CharField(("giá sản phẩm"), max_length=50)
    
    def __str__(self):
        return self.tensanpham

    def __unicode__(self):
        return 

class donhang(models.Model):
    hoadon = models.CharField(("hóa đơn"), max_length=999999)
    sanpham = models.CharField(("sản phẩm khách đặt"), max_length=99999)
    tien = models.CharField(("giá bán"), max_length=999999)
    ngay = models.DateField(("ngày khách đặt"), auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.hoadon

class khachhang(models.Model):
    ten = models.CharField(("Tên khách hàng"), max_length=50,blank=True, null=True)
    sodienthoai = models.CharField(max_length=10, blank=True, null=True)    
    diachi = models.CharField(max_length=9999, blank=True, null=True)
    def __str__(self):
        return self.ten

