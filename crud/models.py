from django.db import models

# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)

    def __str__(self):
        return self.firstname + " " + self.lastname


class DoiTuyen(models.Model):
    name = models.CharField(max_length=40)
    bang = models.CharField(max_length=2)

class LichThiDau(models.Model):
    bang = models.CharField(max_length=2)
    doi1 = models.CharField(max_length=40)
    kq1  = models.CharField(max_length=2)
    doi2 = models.CharField(max_length=40)
    kq2  = models.CharField(max_length=2)
    ngay = models.CharField(max_length=40)
    gio = models.CharField(max_length=40)
    san = models.CharField(max_length=40)


class CauThu(models.Model):
    doituyen = models.CharField(max_length=40)
    ten = models.CharField(max_length=2)
    vitri = models.CharField(max_length=20)
    namsinh = models.CharField(max_length=4)
    chieucao  = models.CharField(max_length=10)
    cannang = models.CharField(max_length=10)