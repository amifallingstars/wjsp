from django.contrib import admin
from .models import Users,Goods,UserOrders,GoodsImg,GoodsHisData
# Register your models here.

class UsersManager(admin.ModelAdmin):
    #展示列表
    list_display=['account','username','password','roles','updated_time']
    #模糊搜索
    search_fields=['username']
    #直接编辑
    list_editable = ['username','password','roles']

class GoodsManager(admin.ModelAdmin):

    list_display = ['id','goodsname','price','seller','start_date','end_date','goods_tags']

    search_fields=['id','goods_tags']

    list_editable=['goodsname','price','start_date','end_date']

class OrderManager(admin.ModelAdmin):
    list_display = ['user','goods','order_No','order_status','order_created_time','order_paid_time']

    search_fields=['user']

    list_editable=['order_status']

class GoodsImgManager(admin.ModelAdmin):
    list_display = ['goods','imgSrc']

class GoodsHisDataManager(admin.ModelAdmin):
    list_display = ['goods','user','data','time']
    search_fields=['user','goods']
    list_editable=['data']


admin.site.register(Users,UsersManager)
admin.site.register(Goods,GoodsManager)
admin.site.register(UserOrders,OrderManager)
admin.site.register(GoodsImg,GoodsImgManager)
admin.site.register(GoodsHisData,GoodsHisDataManager)

# goodsname = models.CharField('商品',max_length=40,null=False)
#     price = models.IntegerField('当前价格',default=0)
#     imgSrc = models.CharField('商品照片',max_length=100,default='http://127.0.0.1:8000/static/goods/0001.jfif')
#     seller = models.ForeignKey('Users',on_delete=models.CASCADE)
#     created_time = models.DateTimeField('商品创建时间',auto_now_add=True)
#     updated_time = models.DateTimeField('商品更新时间',auto_now=True)
#     start_date = models.DateTimeField('起拍时间',default='')
#     end_date = models.DateTimeField('结束拍卖时间',default='')
#     goods_info = models.CharField(max_length=1000,blank=True)  # 商品描述