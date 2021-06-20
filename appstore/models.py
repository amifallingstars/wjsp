from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
# Create your models here.

class Users(models.Model):
    account = models.CharField('用户账号',max_length=20,primary_key=True)
    username = models.CharField('用户名',max_length=40,default='')
    password = models.CharField('用户密码',max_length=16,default='')
    created_time = models.DateTimeField('用户创建时间',auto_now_add=True)
    updated_time = models.DateTimeField('用户更新时间',auto_now=True)
    roles = models.CharField('权限',max_length=10,blank=True)
    phoneNum = models.CharField('手机号',max_length=11,blank=True)
    avatar = models.CharField('头像',max_length=100,default='http://127.0.0.1:8000/static/images/uestc.png')
    qq = models.CharField('QQ账号',max_length=40, blank=True)
    email = models.CharField('邮箱',max_length=40, blank=True)  # 邮箱
    gender = models.CharField('性别',max_length=10, blank=True)
    signature = models.CharField('个性签名',max_length=300,blank=True)
    class Meta:
        verbose_name = '会员账号列表'
        verbose_name_plural = verbose_name

class Goods(models.Model):
    goodsname = models.CharField('商品',max_length=40,null=False)
    price = models.IntegerField('初始价格',default=0)
    highest_price = models.IntegerField('最高价格',default=0)
    # imgSrc = models.CharField('商品照片',max_length=100,default='http://127.0.0.1:8000/static/goods/0001.jfif')
    seller = models.ForeignKey('Users',on_delete=models.CASCADE)
    created_time = models.DateTimeField('商品创建时间',auto_now_add=True)
    updated_time = models.DateTimeField('商品更新时间',auto_now=True)
    start_date = models.DateTimeField('起拍时间',default='')
    end_date = models.DateTimeField('结束拍卖时间',default='')
    goods_info = models.CharField('商品描述',max_length=1000,blank=True)  # 商品描述
    goods_tags = models.CharField('商品标签',max_length=100,default='其他')
    class Meta:
        verbose_name = '竞拍商品列表'
        verbose_name_plural = verbose_name
        db_table = "goods"

class UserToken(models.Model):
    user = models.OneToOneField('Users',on_delete=models.CASCADE)
    token = models.CharField(max_length=300, blank=True)


class UserOrders(models.Model):
    user = models.ForeignKey('Users',on_delete=models.CASCADE)
    goods = models.ForeignKey('Goods',on_delete=models.CASCADE)
    price = models.IntegerField('订单价格',default=0)
    order_No = models.CharField('订单编号',max_length=50,unique=True)
    order_status = models.CharField('订单状态',max_length=20,default='未支付')
    order_created_time = models.DateTimeField('订单创建时间',auto_now=True)
    order_paid_time = models.CharField('订单支付时间',max_length=30,blank=True)
    order_address = models.CharField('收货地址',max_length=100,default='')
    class Meta:
        verbose_name = '订单列表'
        verbose_name_plural = verbose_name

class UserVIP(models.Model):
    user = models.ForeignKey('Users',on_delete=models.CASCADE)
    vip_rank = models.IntegerField('VIP等级',default=0)
    vip_exp = models.IntegerField('VIP当前经验',default=0)

class UserChart(models.Model):
    user = models.ForeignKey('Users',on_delete=models.CASCADE)
    goods = models.ForeignKey('Goods',on_delete=models.CASCADE)
    chart_created_time = models.DateTimeField('加入购物车时间',auto_now_add=True)

class UserFavorites(models.Model):
    user = models.ForeignKey('Users',on_delete=models.CASCADE)
    goods = models.ForeignKey('Goods',on_delete=models.CASCADE)
    fav_created_time = models.DateTimeField('收藏时间',auto_now_add=True)

class GoodsImg(models.Model):
    goods = models.ForeignKey('Goods', on_delete=models.CASCADE)
    imgSrc = models.CharField('商品照片',max_length=100,default='')
    class Meta:
        verbose_name = '商品照片'
        verbose_name_plural = verbose_name

class GoodsHisData(models.Model):
    user = models.ForeignKey('Users',on_delete=models.CASCADE)
    goods = models.ForeignKey('Goods',on_delete=models.CASCADE)
    data = models.IntegerField('竞价',default=0)
    time = models.DateTimeField('竞拍时间',auto_now_add=True)
    class Meta:
        verbose_name = '历史竞价'
        verbose_name_plural = verbose_name
