from django.shortcuts import render,redirect
from .models import FoodTypes,Goods,Wheel,Nav,Mustbuy,Shop,MainShow,User
# Create your views here.

def home(request):
    wheelsList = Wheel.objects.all()
    topNavList = Nav.objects.all()
    mustbuyList = Mustbuy.objects.all()
    shopList = Shop.objects.all()
    shop1 = shopList[0]
    shop2 = shopList[1:3]
    shop3 = shopList[3:7]
    shop4 = shopList[7:11]
    mainList = MainShow.objects.all()

    return render(request,'axf/home.html',{'wheelsList':wheelsList,'navList':topNavList,'mustbuyList':mustbuyList,'shop1':shop1,'shop2':shop2,'shop3':shop3,'shop4':shop4,'mainList':mainList})
#超市
def market(request,categoryId,cid,sortid):
    leftSlider = FoodTypes.objects.all()
    print('------>',cid)
    if cid == '0':
        #全部分类
        productList = Goods.objects.filter(categoryid=categoryId)
    else:
        productList = Goods.objects.filter(categoryid=categoryId,childcid=cid)

    if sortid == '1':
        productList = productList.order_by("productnum")
    elif sortid == '2':
        productList = productList.order_by("price")
    elif sortid == '3':
        productList = productList.order_by("-price")

    childList = []
    group = leftSlider.get(typeid=categoryId)
    chilenames = group.childtypenames
    arr1 = chilenames.split('#')
    for str in arr1:
        arr2 = str.split(':')
        obj = {'childName':arr2[0],'childId':arr2[1]}
        childList.append(obj)

    return render(request,'axf/market.html',{'leftSlider':leftSlider,'productList':productList,'childList':childList,'categoryid':categoryId,'cid':cid,'sortid':sortid})
#购物车
def cart(request):
    return render(request,'axf/cart.html')
#我的
def mine(request):

    return render(request,'axf/mine.html')

#登录
from .froms.login import LoginForm
def login(request):
    if request.method == 'POST':
        f = LoginForm(request.POST)
        if f.is_valid():
            return redirect('/mine/')
        else:
            return render(request, 'axf/login.html', {"title": "登陆", "form": f, "error": f.errors})

    f = LoginForm()
    return render(request,'axf/login.html',{'title':'登录','form':f})

def register(request):
   return render(request,'axf/register.html')

from django.http import JsonResponse
def checkUserId(request):
    userid = request.POST.get('userid')
    try:
        user = User.objects.get(userAccount=userid)
        return JsonResponse({'data':'该用户已经被注册','status':'error'})
    except User.DoesNotExist as e:
        return JsonResponse({'data':'可以注册','status':'success'})
