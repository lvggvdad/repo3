from django.shortcuts import render
from django.template import loader,RequestContext
from django.http import HttpResponse,JsonResponse
from django.conf import settings
from booktest.models import PicTest,AreaInfo
# Create your views here.


def my_render(request,template_path,context={}):
    #1.加载模板文件，获取一个模板对象
    temp=loader.get_template('booktest/index.html')
    #2.定义模板上下文，给模板文件传数据
    context=RequestContext(request,{})
    #3.模板渲染，产生一个替换后的html内容
    res_html=temp.render(context)
    #4.返回应答
    return HttpResponse(res_html)
# /index
def index(request):
    '''首页'''
    #获取浏览器端的ip地址
    user_ip= request.META['REMOTE_ADDR']
    print (user_ip)
    return render(request,'booktest/index2.html')

# /static_test
def static_test(request):
    '''静态文件'''
    print(settings.STATICFILES_FINDERS)
    return  render(request,'booktest/index.html')

# /show_upload
def show_upload(request):
    '''显示上传图片页面'''
    return render(request,'booktest/upload_pic.html')

# /upload_handle
def upload_handle(request):
    '''上传图片处理'''
    #1.获取上传的图片
    request.FILES['pic']

    #2.创建一个文件
    save_path='%s/booktest/%s'%(settings.MEDIA_ROOT,pic,name)
    with open(save_path,'wb') as f :
        #3.获取上传文件的内容，并写到创建的文件中
        for content in pic.chunks():
            f.write(content)
    #4.在数据库中保存上传记录
    PicTest.objects.create(goods_pic='booktest/%s'%pic.name)
    #5.返回
    return HttpResponse('ok')

# /show_area
from django.core.paginator import Paginator
def show_area(request):
    '''分页'''
    #1.查询出所有省级地区的信息
    areas=AreaInfo.objects.filter(aParent__isnull=True)
    #2.分页，每页显示10条
    paginator=Paginator(areas,10)
    #3.获取第一页的内容
    #page是Page类的实例对象
    page=paginator.page(1)
    #4.使用模板

    return render(request,'booktest/show_area.html',{'page':page})

# /areas
def areas(request):
    '''省市县选中案例'''
    return render(request,'booktest/areas.html')

def prov(request):
    '''获取所有省级地区的信息'''
    #1.获取所有省级地区的信息
    areas = AreaInfo.objects.filter(aParent__isnull=True)
    #2.变量areas并拼接出json数据:标题:atitle id
    areas_list=[]
    for area in areas:
        areas_list.append((area.id, area.atitle))
    #2.返回数据
    return  JsonResponse({'data':areas_list})

def city(request,pid):
    '''获取pid的下级地区的信息'''
    # area=AreaInfo.objects.get(id=pid)
    #areas=area.areainfo_set.all()
    areas=AreaInfo.objects.filter(aParent__id=pid)

    #2.变量areas并拼接出json数据:标题:atitle id
    areas_list=[]
    for area in areas:
        areas_list.append((area.id, area.atitle))
    #2.返回数据
    return  JsonResponse({'data':areas_list})

