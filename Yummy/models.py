# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class GoodsDetail(models.Model):
    goods_id = models.AutoField(primary_key=True)
    pic = models.CharField(max_length=255)
    goods_name = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    stock = models.IntegerField()
    flvoar = models.CharField(max_length=255)
    strocon = models.CharField(max_length=255)
    deliran = models.CharField(max_length=255)
    component = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    tips = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_detail'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=1024)
    tel = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    qq = models.CharField(db_column='QQ', max_length=255)  # Field name made lowercase.
    wechat = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'

