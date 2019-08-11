#coding:utf8
from django.conf.urls import include, url
from django.contrib import admin
from stumanage import views
#处理媒体文件的API
from django.views.static import serve
#把django的配置文件导进来
from django.conf import settings
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.index,name='index'),
    url(r'^stu_del/$',views.stu_del,name='stu_del'),
    url(r'^movie/$',views.movie_index,name='movie'),

    url(r'^stu_add/$',views.stu_add,name='stu_add'),
    url(r'^cls_edit/$',views.cls_edi,name='cls_edit'),
    url(r'^cls_add/$',views.cls_add,name='cls_add'),
    url(r'^cls_index/$',views.cls_index,name='cls_index'),
    url(r'^cls_del/$',views.cls_del,name='cls_del'),
    url(r'^stu_edit/$',views.stu_edit,name='stu_edit'),
    url(r'^login/$',views.login,name='login'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^reg/$',views.reg,name='reg'),

    #写一个媒体文件的url，并且用serve函数处理，指定媒体文件的路径
    url(r'^upload/(.*)$',serve,{'document_root':settings.MEDIA_ROOT}),

]
