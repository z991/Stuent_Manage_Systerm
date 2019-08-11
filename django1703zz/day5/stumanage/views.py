#coding:utf8
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from stumanage import models
#做判断条件,一个Q就是一个条件，然后用并集操作符连接
from django.db.models import Q, F
#                                 分页类       非法页       空页         页数不是整型
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from django.contrib import auth#登录，退出，验证
from django.contrib.auth.decorators import login_required#必须通过登录才能进入管理学生界面
from django.contrib.auth.models import User#导入用户表
from django.contrib.auth.hashers import make_password#给密码加密
import os
#生成唯一标识符
import uuid


@login_required
def index(request):
    #搜索，如果没有关键字，列出所有结果
    wd=request.GET.get('wd',None)
    order=request.GET.get('order',None)
    rule=request.GET.get('rule',None)
    pn=request.GET.get('pn',1)
    #pn不是数字转成整型
    try:
        pn=int(pn)
    except Exception as e:
        pn=1
    if wd is not None:
        conditon=Q(name__icontains=wd) | Q(score__icontains=wd) | Q(age__icontains=wd) | Q (email__icontains=wd) | Q(cls__name__icontains=wd)
        stus=models.Student.objects.filter(conditon)
    else:
        stus = models.Student.objects.all()

    #排序规则处理
    if order is not None:
        if rule == 'u':#升序
            stus=stus.order_by(order)
        else:#降序
            stus=stus.order_by(order).reverse()
    #分页
    try:
        paginator=Paginator(stus,2)
        stus = paginator.page(pn)
    except (InvalidPage,EmptyPage,PageNotAnInteger) as e:
        pn=1
        stus = paginator.page(pn)
        print(e)
    #分页数字生成
    num_pages=stus.paginator.num_pages
    if num_pages<3:
       start=1
       end=num_pages+1
    else:

        if pn <=2:#页数左边界
            start=1
            end=4
        elif pn>=num_pages-2:#页数右边界
            start=num_pages-2
            end=num_pages+1
        else:#页数不触及边界的情况
            start=pn-1
            end=pn+2

    page_nums = range(start,end)
    context={
        'index':'active',
        'stus':stus,
        'wd':wd,
        'page_nums':page_nums,
    }
    return render(request,'stumanage/index.html',context)

#删除学生
def stu_del(request):
    sid = request.GET.get('sid', None)
    models.Student.objects.filter(pk=sid).delete()
    return HttpResponseRedirect('/')

#上传文件
def upload(request,file):#file就是上传的文件
    if file.size/1024/1024 < 2:#判断文件上传大小
        if file.content_type == 'image/jpeg' or file.content_type == 'image/gif':
            #把文件存到服务器上
            #按照文件名的.分割，然后取文件的后缀名
            new_name=str(uuid.uuid4())+'.'+file.name.split('.')[-1]
            fname='upload/avatar/'+new_name
            dirname=os.path.dirname(fname)#获取路径名称
            if not os.path.exists(dirname):#不存在路径
                os.makedirs(dirname)

            with open(fname,'wb') as f:#写入方式打开
                if file.multiple_chunks():#多块文件
                    for chunck in file.chunks():#遍历文件的所有块
                        f.write(chunck)
                else:#单块文件
                    f.write(file.read())
            return True,new_name #上传成功返回True和文件的姓名字
        else:
            return False,'文件类型只能是jpeg或者gif'
    else:
        return False,'文件不能超过2M'



#添加学生业务处理
def stu_add(request):
    if request.method=='POST':
        name=request.POST.get('name',None)
        age = request.POST.get('age', None)
        score = request.POST.get('score', None)
        email = request.POST.get('email', None)
        cls_id = request.POST.get('cls', None)
        # 通过FILES字典获取单个上传文件，avatar是通过模板变量里的input标签的name属性决定的
        avatar=request.FILES.get('avatar',None)#获取一个文件对象
        if avatar is not None:
            res=upload(request,avatar)
            if res[0] is False:
                return render(request,'stumanage/stu_add.html',{'error':res[1]})
            else:#上传成功
                new_name=res[1]#获取返回的新名字
        stu_info={
            'name':name,
            'age':age,
            'score':score,
            'email':email,
            'cls_id':cls_id,
            'avatar':'avatar/'+new_name,
        }
        models.Student.objects.create(**stu_info)
        return HttpResponseRedirect('/')
    else:
        classes=models.Class.objects.all()
        context = {
            'manage': 'active',
            'classes':classes,
        }
        return render(request,'stumanage/stu_add.html',context)

def cls_add(request):
    if request.method == 'POST':
        cls_name = request.POST.get('cls_name')
        print('cls_name===', cls_name)
        exists = models.Class.objects.filter(name=cls_name).exists()
        if exists == True:
            return render(request, 'stumanage/class_add.html', {'error': '该班级{}已存在'.format(cls_name)})
        models.Class.objects.create(**{"name": cls_name})
        return HttpResponseRedirect('/cls_index/')
    else:
        context = {
            'cls_manage': 'active'
        }
        return render(request, 'stumanage/class_add.html', context)

def cls_edi(request):
    cl_id = request.GET.get('cl_id', None)
    if request.method == 'POST':
        cls_name = request.POST.get('cls_name')
        exists = models.Class.objects.filter(name=cls_name).exists()
        if exists == True:
            return render(request, 'stumanage/class_add.html', {'error': '该班级{}已存在'.format(cls_name)})
        models.Class.objects.filter(id=cl_id).update(**{"name": cls_name})
        return HttpResponseRedirect('/cls_index/')
    else:
        cls = models.Class.objects.get(id=cl_id)
        return render(request, 'stumanage/class_add.html', {"cls": cls})

def cls_del(request):
    cl_id = request.GET.get('cl_id', None)
    models.Class.objects.filter(pk=cl_id).delete()
    return HttpResponseRedirect('/cls_index/')

def cls_index(request):
    #搜索，如果没有关键字，列出所有结果
    wd=request.GET.get('name',None)
    order=request.GET.get('order',None)
    rule=request.GET.get('rule',None)
    pn=request.GET.get('pn',1)
    #pn不是数字转成整型
    try:
        pn=int(pn)
    except Exception as e:
        pn=1
    if wd is not None:
        cls=models.Class.objects.filter(name__icontains=wd)
    else:
        cls = models.Class.objects.all()

    #排序规则处理
    if rule == 'd':
        cls = cls.order_by('name').reverse()
    else:#降序
        cls=cls.order_by('name')
    #分页
    try:
        paginator=Paginator(cls,2)
        stus = paginator.page(pn)
    except (InvalidPage,EmptyPage,PageNotAnInteger) as e:
        pn=1
        stus = paginator.page(pn)
        print(e)
    #分页数字生成
    num_pages=stus.paginator.num_pages
    if num_pages<3:
       start=1
       end=num_pages+1
    else:

        if pn <=2:#页数左边界
            start=1
            end=4
        elif pn>=num_pages-2:#页数右边界
            start=num_pages-2
            end=num_pages+1
        else:#页数不触及边界的情况
            start=pn-1
            end=pn+2

    page_nums = range(start,end)
    context={
        'cls_index':'active',
        'cls':cls,
        'wd':wd,
        'page_nums':page_nums,
    }
    return render(request,'stumanage/class_index.html',context)


@login_required
def movie_index(request):
    #搜索，如果没有关键字，列出所有结果
    print('data===', request.GET)
    wd=request.GET.get('wd',None)
    order = request.GET.get('order', None)
    rule=request.GET.get('rule',None)
    pn=request.GET.get('pn',1)
    #pn不是数字转成整型
    try:
        pn=int(pn)
    except Exception as e:
        pn=1
    if wd not in ['None', None]:
        conditon=Q(name__icontains=wd) | Q(actor__icontains=wd)
        movie=models.Movie.objects.filter(conditon)
    else:
        movie = models.Movie.objects.all()

    #排序规则处理
    if order is not None:
        if rule == 'u':#升序
            movie=movie.order_by(order)
        else:#降序
            movie=movie.order_by(order).reverse()
    #分页
    try:
        paginator=Paginator(movie,10)
        movie = paginator.page(pn)
    except (InvalidPage,EmptyPage,PageNotAnInteger) as e:
        pn=1
        movie = paginator.page(pn)
        print(e)
    #分页数字生成
    num_pages=movie.paginator.num_pages
    if num_pages<3:
       start=1
       end=num_pages+1
    else:

        if pn <=2:#页数左边界
            start=1
            end=4
        elif pn>=num_pages-2:#页数右边界
            start=num_pages-2
            end=num_pages+1
        else:#页数不触及边界的情况
            start=pn-1
            end=pn+2

    page_nums = range(start,end)
    context={
        'movie_':'active',
        'movie': movie,
        'wd':wd,
        'page_nums':page_nums,
    }
    return render(request,'stumanage/movie.html',context)


#学生修改业务处理
def stu_edit(request):
    sid=request.GET.get('sid',None)
    if request.method=='POST':
        name=request.POST.get('name',None)
        age=request.POST.get('age',None)
        score=request.POST.get('score',None)
        email=request.POST.get('email',None)
        cls_id=request.POST.get('cls',None)

        avatar=request.FILES.get('avatar',None)#获取一个文件对象
        if avatar is not None:
            res=upload(request,avatar)
            if res[0] is False:
                return render(request,'stumanage/stu_add.html',{'error':res[1]})
            else:#上传成功
                new_name=res[1]#获取返回的新名字
        stu_info={
            'name':name,
            'age':age,
            'score':score,
            'email':email,
            'cls_id':cls_id,
            'avatar':'avatar/'+new_name,
        }
        models.Student.objects.filter(id=sid).update(**stu_info)
        return HttpResponseRedirect('/')
    else:
        stu=models.Student.objects.get(id=sid)
        classes=models.Class.objects.all()
        return render(request,'stumanage/stu_add.html',{'stu':stu,'classes':classes})

#登录
def login(request):
    if request.method == 'POST':
        username=request.POST.get('username',None)
        password=request.POST.get('password',None)
        if username and password:
            user=auth.authenticate(username=username,password=password)#如果验证成功返回用户对象，如果不成功返回None
            if user is not None:
                if user.is_active:
                    #做登录操作
                    auth.login(request,user)
                    return HttpResponseRedirect('/')
                else:
                    return render(request,'stumanage/login.html',{'error':'帐号已冻结'})
            else:
                return render(request,'stumanage/login.html',{'error':'用户名或者密码错误'})


    else:
        pass
    return render(request,'stumanage/login.html')

#退出操作
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')


#注册操作
def reg(request):
    if request.method == 'POST':
        #收集用户信息
        username=request.POST.get('username',None)
        password1 = request.POST.get('password1', None)
        password2 = request.POST.get('password2', None)
        nick = request.POST.get('nick', '')
        phone = request.POST.get('phone', '')
        if username and password1 and password2:
            if password1 == password2:
                u_count=User.objects.filter(username=username).count()
                if u_count == 0:#没有这个用户名
                    #添加自带用户表
                    user_info={
                        'username':username,
                        'password':make_password(password1)
                    }
                    user_info=User.objects.create(**user_info)

                    #添加用户拓展信息
                    user_profile={
                        'nick':nick,
                        'phone':phone,
                        'user':user_info
                    }
                    models.UserProfile.objects.create(**user_profile)
                    return HttpResponseRedirect('/login/')
                else:#用户名已经存在
                    return render(request,'stumanage/reg.html',{'error':'用户名已经存在'})


            else:
                return render(request,'stumanage/reg.html',{'error':'两次密码不一样'})

    return render(request,'stumanage/reg.html')