import os
import random
import uuid
import time
import datetime

from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse

from django.conf import settings
# from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from rest_framework.authtoken.models import Token
# Create your views here.
from appstore.models import UserOrders, Users,UserToken,Goods,GoodsImg
from appstore import models

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC = settings.STATICFILES_DIRS

def update_price(item):
    if item.highest_price < item.price:
                item.highest_price = item.price
                item.save()
    return 

def Token_encode(data):
    import jwt
    import time

    tic = time.time()
    payload = {
                'exp': tic+60*60,# Expiration Time 此token的过期时间的时间戳
                'iss':'UESTC',# (Issuer) Claim 指明此token的签发者
                'aud':'users',#(Audience) Claim 指明此token签发面向群体
                'account': data,
                'iat': tic # (Issued At) Claim 指明此创建时间的时间戳
                }
    secret = 'UESTC'
    token = jwt.encode(payload,
                   secret,  # key
                   algorithm='HS256')
    return token


class AppViewSet(viewsets.ModelViewSet):

    def register(self,request):
        account = request.data.get('account')  # 获取账号
        # 判断账号是否已经存在
        users = Users.objects.filter(account=account)
        if len(users) > 0:
            return JsonResponse({'status': 401, 'msg': '账号已存在！'})
        # 先获取前台传来的登录信息
        username = request.data.get('username')  # 获取用户名（昵称）
        password = request.data.get('password')  # 获取密码
        gender = request.data.get('gender')  # 获取性别
        phoneNum = request.data.get('phoneNum')  # 获取电话号码
        roles = request.data.get('roles')  # 获取权限
        email = request.data.get('email')  # 获取邮箱
        user = Users(
            account = account,
            username = username,
            password = password,
            roles = roles,
            phoneNum = phoneNum,
            avatar = 'http://127.0.0.1:8000/static/images/0002.GIF',
            qq = '',
            email = email,
            gender = gender,
            signature = '',
        )
        user.save()
        res = {'code': 0, 'msg': '',
            'data':{
                'token':'',
            }
            }
        res['code'] = 200
        res['msg'] = '注册成功'

        token  =  Token_encode(account)
        res['data']['token'] = token
        # print(token)
        models.UserToken.objects.update_or_create(user=user,defaults={'token':token})

        return JsonResponse(res)

    def login(self,request):
    # 先获取前台传来的登录信息
        try:
            account = request.data.get('account')
            password = request.data.get('password')
        except:
            account = None
            password = None
        print(account,password)
        res = {'code': 0, 'msg': '',
            'data':{
                'token':'',
            }
            }
        ACC = Users.objects.filter(account=account,password=password)
        if ACC:
            res['code'] = 200
            res['msg'] = '登陆成功'
        else:
            res['code'] = 401
            res['msg'] = '用户名或密码错误，请重试'
            return JsonResponse(res)

        token  =  Token_encode(account)
        res['data']['token'] = token
        # print(token)
        models.UserToken.objects.update_or_create(user=ACC.first(),defaults={'token':token})

        return JsonResponse(res)

    def getUserinfo(self,request):
        token = request.GET.get('token')
        try:
            user = UserToken.objects.get(token=token)
        except:
            user = None
        if user:
            user = user.user
            res = {
                'code': 200, 
                'msg': '请求成功',
                'data':{
                    'roles':user.roles,
                    'signature':user.signature,
                    'avatar':user.avatar,
                    'name':user.username,
                    'qq':user.qq,
                    'email':user.email,
                    'phoneNum':user.phoneNum
                }
            }
        else:
            res = {
                'code': 401, 
                'msg': '未登录',
            }

        return JsonResponse(res)

    # 更新用户信息
    def updateUserinfo(self,request):
        token = request.META.get('HTTP_X_TOKEN')
        try:
            user = UserToken.objects.get(token=token)
        except:
            user = None
        if user is None:  # 如果查询到空
            return JsonResponse({'code': 405, 'msg': "token验证失败"})
        user=user.user
        try:
            # 读取请求
            userInfo = request.data.get('userInfo')
            username = userInfo['name']
            signature = userInfo['signature']
            email = userInfo['email']
            qq = userInfo['qq']
            phoneNum = userInfo['phoneNum']
            
        except:
            res = {
                'code': 401, 
                'msg': '请求错误',
            }
            return JsonResponse(res)
        # 更新用户信息
        user.username = username
        user.signature = signature
        user.email = email
        user.qq = qq
        user.phoneNum = phoneNum
        user.save()
        return JsonResponse({'code': 200, 'msg': "更新成功"})

    def logout(self,request):
        res = {
            'code':200,
            'msg': 'sucess',
            }
        return JsonResponse(res)
    # 添加商品
    def addgoods(self,request):
        try:
            token = request.META.get('HTTP_X_TOKEN')
            user = UserToken.objects.get(token=token)
            user = user.user
        except :
            res = {'code': 401, 'msg': "请求失败"}
            return JsonResponse(res)
        print(request.data)
        goodsname = request.data.get('goodsname')  # 获取用户名（昵称）
        price = request.data.get('price')  # 获取密码
        seller = user 
        start_date = request.data.get('start_date')  # 获取权限
        end_date = request.data.get('end_date')  # 获取邮箱
        goods_info = request.data.get('goods_info')
        goods_tags = request.data.get('goods_tags')
        goods = Goods(
            goodsname = goodsname,
            price = price,
            highest_price = price,
            seller = seller,
            start_date = start_date,
            end_date = end_date,
            goods_info = goods_info,
            goods_tags = goods_tags,
        )
        goods.save()
        res = {'code': 200, 'msg': "添加成功" ,'data':goods.id}
        return JsonResponse(res)

    def uploadimg(self,request):
        try:
            token = request.META.get('HTTP_X_TOKEN')
            user = UserToken.objects.get(token=token)
            user = user.user
        except :
            res = {'code': 401, 'msg': "请求失败"}
            return JsonResponse(res)
        try:  
            
            file = request.FILES.get('file')
            id = request.data.get('goodsid')
            uid = request.data.get('uid')
            goods = models.Goods.objects.get(id=id)
            print(file.name)
            # 构造图片保存路径
            file_path = 'E:/工作站/软件工程/项目/backend/wjsp/static/goods/' + str(goods.id)
            if not os.path.exists(file_path):  # 如果目录不存在则创建
                os.mkdir(file_path)
            file_path = file_path+'/' + str(uid) +file.name
            # 保存图片
            try:
                with open(file_path, 'wb+') as f:
                    f.write(file.read())
                    f.close()
            except Exception as e:
                print(e)
            file_path = 'http://127.0.0.1:8000/static/goods/' + str(goods.id)+'/' + str(uid) +file.name
            models.GoodsImg.objects.create(goods=goods,imgSrc=file_path)
            res = {'code': 200, 'msg': "添加成功"}
        except Exception as err:
            print(err)
            res = {'code': 401, 'msg': "添加失败"}
        
            
        
        return JsonResponse(res)
        

    def getGoodslist(self,request):
        if request is None:
            res ={'code': 401, 'msg': "请求失败"}
            return JsonResponse(res)
        queryInfo = request.data.get('queryInfo')
        pgs = queryInfo['pageSize']
        pgN = queryInfo['pageNum']
        res = {'code': 200, 'msg': "更新成功",'data':[],'tag':0}
        if queryInfo['flag']:
            pgN = 1
        if queryInfo['query'] is not None:
            goods = models.Goods.objects.filter(goodsname__contains=queryInfo['query'])
        else: 
            goods = models.Goods.objects.all()
        if queryInfo['select'] is not None:
            goods = goods.filter(goods_tags__contains=queryInfo['select'])
            # print(goods)
            print(len(goods))
        now = datetime.datetime.now()
        #前一天
        start = now

        # start = now+datetime.timedelta(day=-1)
        goods=goods.filter(end_date__gt=start)
        goods=goods.filter(start_date__lt=start)

        # 查询数据库
        # item = models.Goods
        # Goods = item.objects.all()
        print(start)
        for i in range((pgN-1)*pgs,min((pgN)*pgs,len(goods))):
        # for item in goods:
            item = goods[i]
            dict = {}
            update_price(item)
            item.start_date = int(time.mktime(item.start_date.timetuple())*1000) + 8*60*60*1000
            item.end_date = int(time.mktime(item.end_date.timetuple())*1000) + 8*60*60*1000
            tmp = int(time.time()*1000) 
            if tmp>item.end_date or tmp<item.start_date:
                Len=Len-1
                continue
            imgSrc = models.GoodsImg.objects.filter(goods=item)[0]
            dict['id'] = item.id
            dict["goodsname"] = item.goodsname
            dict['price'] = max(item.price,item.highest_price)
            dict['imgSrc'] = imgSrc.imgSrc
            dict['seller'] = item.seller.username
            dict['start_time'] = item.start_date
            dict['end_time'] = item.end_date
            dict['goods_info'] = item.goods_info
            dict['time_diff'] = item.end_date - item.start_date
            res['data'].append(dict) 
        res['total'] = len(goods)
        return JsonResponse(res)

    def getOneGoods(self,request):
        try:
            id = request.data.get('id')
        except :
            res = {'code': 401, 'msg': "请求失败"}
        goods = models.Goods.objects.filter(id=id).first()
        update_price(goods)
        imgSrc = models.GoodsImg.objects.filter(goods=goods)
        goods.start_date = int(time.mktime(goods.start_date.timetuple())*1000) + 8*60*60*1000
        goods.end_date = int(time.mktime(goods.end_date.timetuple())*1000) + 8*60*60*1000
        if goods.highest_price < goods.price:
                goods.highest_price = goods.price
                goods.save()
        dict = {
            'imgSrc' :[],
        }
        dict['id'] = goods.id
        dict["goodsname"] = goods.goodsname
        dict['price'] = max(goods.price,goods.highest_price)
        dict['seller'] = goods.seller.username
        dict['start_time'] = goods.start_date
        dict['end_time'] = goods.end_date
        dict['goods_info'] = goods.goods_info
        dict['time_diff'] = goods.end_date - goods.start_date
        for img in imgSrc:
            dict['imgSrc'].append(img.imgSrc)
        res = {'code': 200, 'msg': "更新成功",'data':dict}
        return JsonResponse(res)

    

    def getChartdata(self,request):
        print(request.data)
        id = request.data.get('id')
        goods = models.Goods.objects.filter(id=id).first()
        price = goods.price
        Data = [(price,"无人出价")]*7
        hisdata = models.GoodsHisData.objects.filter(goods=goods)
        for data in hisdata:
            Data.append((data.data,data.user.username))
        
        Data.sort(reverse=True)
        res={'code': 200, 'msg': "更新成功",'data':Data}
        return JsonResponse(res)

    def getprice(self,request):
        try:
            token = request.META.get('HTTP_X_TOKEN')
            user = UserToken.objects.get(token=token)
            user = user.user
        except :
            res = {'code': 401, 'msg': "请求失败"}
            return JsonResponse(res)
        id = request.data.get('id')
        price = request.data.get('price')
        goods = models.Goods.objects.filter(id=id).first()
        update_price(goods)
        models.GoodsHisData.objects.create(goods=goods,user=user,data=price)
        goods.highest_price = price
        goods.save()
        res={'code': 200, 'msg': "竞价成功成功"}
        return JsonResponse(res)

    def generate_order(self,request):
        try:
            token = request.META.get('HTTP_X_TOKEN')
            user = UserToken.objects.get(token=token)
            user = user.user
        except :
            res = {'code': 401, 'msg': "请求失败"}
        id = request.data.get('id')
        price = request.data.get('price')
        print('1')
        goods = models.Goods.objects.filter(id=id).first()
        print('2')
        try:
            orders = models.UserOrders.objects.get(user=user,goods=goods)
        except :
            orders = None
        print('3')
        print(orders)
        if orders is None:
            orders = UserOrders(
                user = user,
                goods = goods,
                price = price,
                order_No = user.account + str(goods.id),
                order_status = '拍卖进行中', 
                order_address = '',
                order_paid_time = '',
            )
            print('4')
        else:
            print('5')
            orders.price = price
            orders.order_status = '拍卖进行中'
        orders.save()
        res={'code': 200, 'msg': "订单已生成"}
        return JsonResponse(res)

    def getOrderlist(self,request):
        try:
            token = request.META.get('HTTP_X_TOKEN')
            user = UserToken.objects.get(token=token)
            user = user.user
        except :
            res = {'code': 401, 'msg': "请求失败"}
            return JsonResponse(res)
        res = {'code': 200, 'msg': "更新成功",'data':[]}
        Orders = models.UserOrders.objects.filter(user=user)
        
        for item in Orders:
            dict = {}
            imgSrc = models.GoodsImg.objects.filter(goods=item.goods).first()
            dict['order_No'] = item.order_No
            dict['order_status'] = item.order_status
            dict['order_created_time'] = item.order_created_time
            dict['order_price'] = item.price
            dict['goodsname'] = item.goods.goodsname
            dict['imgSrc'] = imgSrc.imgSrc
            dict['price'] = item.goods.price
            dict['seller'] = item.goods.seller.username
            res['data'].append(dict) 
        return JsonResponse(res)


    def updateavatar(self,request):
        
        try:
            token = request.META.get('HTTP_X_TOKEN')
            user = UserToken.objects.get(token=token)
            user = user.user
        except :
            res = {'code': 401, 'msg': "请求失败"}
            return JsonResponse(res)
        try:  
            
            file = request.data.get('avatar')
            print(file.name)
            # 构造图片保存路径
            file_path = STATIC[0]+ os.sep +'users'+ os.sep + str(user.account)
            print(file_path)
            if not os.path.exists(file_path):  # 如果目录不存在则创建
                os.mkdir(file_path)
            file_path = file_path+'/' + str(file.name)
            # 保存图片
            print(1)
            try:
                with open(file_path, 'wb+') as f:
                    f.write(file.read())
                    f.close()
            except Exception as e:
                print(e)
            file_path = 'http://127.0.0.1:8000/static/users/' + str(user.account)+'/' + str(file.name)
            # models.GoodsImg.objects.create(goods=goods,imgSrc=file_path)
            user.avatar = file_path
            user.save()
            res = {'code': 200, 'msg': "添加成功", 'data':file_path}
        except Exception as err:
            print(err)
            res = {'code': 401, 'msg': "添加失败"}

        return JsonResponse(res)

        


   
        
