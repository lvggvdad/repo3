
from django.conf.urls import  url
from booktest import views

urlpatterns = [
    url(r'^index$',views.static_test),
    url(r'^index2$',views.index),
    url(r'^show_upload$',views.show_upload),#显示上传图片
    url(r'^show_area$',views.show_area),#分页
    url(r'^areas$',views.areas),#省市县选中案例
    url(r'^prov$',views.prov),#获取省级地区的信息
    url(r'^city(\d+)$',views.city),#获取省级下面市级地区的信息
    url(r'^dis(\d+)$',views.city),#获取省级下面市级地区的信息
]
