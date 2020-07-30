from django.shortcuts import render
from .models import Products, Userlogin


# Create your views here.
def index(request):
    products = Products.objects.all()
    print(products)
    params = {'products': products}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/aboutus.html')


def contact(request):
    return render(request, 'shop/contactus.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')


def productview(request):
    products = Products.objects.all()
    return render(request, 'shop/productview.html', {'products': products})


def checkout(request):
    return render(request, 'shop/checkout.html')


def privacypolicy(request):
    return render(request, 'shop/privacypolicy.html')


def termscondition(request):
    return render(request, 'shop/term&condition.html')


def ultra(request):
    products = Products.objects.all()
    print(products)
    params = {'products': products}
    return render(request, 'shop/ultra.html', params)


def productdetails0(request):
    products = Products.objects.all()
    print(products)
    params = {'products': products}
    return render(request, 'shop/productdetails0.html', params)


def productdetails1(request):
    products = Products.objects.all()
    print(products)
    params = {'products': products}
    return render(request, 'shop/productdetails1.html', params)


def productdetails2(request):
    products = Products.objects.all()
    print(products)
    params = {'products': products}
    return render(request, 'shop/productdetails2.html', params)


def productdetails3(request):
    products = Products.objects.all()
    print(products)
    params = {'products': products}
    return render(request, 'shop/productdetails.html3', params)


def productdetails4(request):
    products = Products.objects.all()
    print(products)
    params = {'products': products}
    return render(request, 'shop/productdetails4.html', params)


def productdetails5(request):
    products = Products.objects.all()
    print(products)
    params = {'products': products}
    return render(request, 'shop/productdetails5.html', params)


def productdetails6(request):
    products = Products.objects.all()
    print(products)
    params = {'products': products}
    return render(request, 'shop/productdetails6.html', params)


def productdetails7(request):
    products = Products.objects.all()
    print(products)
    params = {'products': products}
    return render(request, 'shop/productdetails7.html', params)


def productdetails8(request):
    products = Products.objects.all()
    print(products)
    params = {'products': products}
    return render(request, 'shop/productdetails8.html', params)


def productdetails9(request):
    products = Products.objects.all()
    print(products)
    params = {'products': products}
    return render(request, 'shop/productdetails9.html', params)


def productdetails10(request):
    products = Products.objects.all()
    print(products)
    params = {'products': products}
    return render(request, 'shop/productdetails10.html', params)


def productdetails11(request):
    products = Products.objects.all()
    print(products)
    params = {'products': products}
    return render(request, 'shop/productdetails11.html', params)


def productdetails12(request):
    products = Products.objects.all()
    print(products)
    params = {'products': products}
    return render(request, 'shop/productdetails12.html', params)


def productdetails13(request):
    products = Products.objects.all()
    print(products)
    params = {'products': products}
    return render(request, 'shop/productdetails13.html', params)


def productdetails14(request):
    products = Products.objects.all()
    print(products)
    params = {'products': products}
    return render(request, 'shop/productdetails.html14', params)


def productdetails15(request):
    products = Products.objects.all()
    print(products)
    params = {'products': products}
    return render(request, 'shop/productdetails15.html', params)


def productdetails16(request):
    products = Products.objects.all()
    print(products)
    params = {'products': products}
    return render(request, 'shop/productdetails16.html', params)


def productdetails17(request):
    products = Products.objects.all()
    print(products)
    params = {'products': products}
    return render(request, 'shop/productdetails17.html', params)


def productdetails18(request):
    products = Products.objects.all()
    print(products)
    params = {'products': products}
    return render(request, 'shop/productdetails18.html', params)


def productdetails19(request):
    products = Products.objects.all()
    print(products)
    params = {'products': products}
    return render(request, 'shop/productdetails19.html', params)


def productdetails20(request):
    products = Products.objects.all()
    print(products)
    params = {'products': products}
    return render(request, 'shop/productdetails20.html', params)


def productdetails21(request):
    products = Products.objects.all()
    print(products)
    params = {'products': products}
    return render(request, 'shop/productdetails21.html', params)


def productdetails22(request):
    products = Products.objects.all()
    print(products)
    params = {'products': products}
    return render(request, 'shop/productdetails22.html', params)


def productdetails23(request):
    products = Products.objects.all()
    print(products)
    params = {'products': products}
    return render(request, 'shop/productdetails23.html', params)


def ultracartridges(request):
    products = Products.objects.all()
    print(products)
    params = {'products': products}
    return render(request, 'shop/ULTRA Cartridges.html', params)


def neo(request):
    products = Products.objects.all()
    print(products)
    params = {'products': products}
    return render(request, 'shop/neo.html', params)


def neocartridges(request):
    products = Products.objects.all()
    print(products)
    params = {'products': products}
    return render(request, 'shop/NEO Cartridges.html', params)


def cart(request):
    return render(request, 'shop/cart.html')


def signin(request):
    user = Userlogin.objects.all()
    print(user)
    params = {'users': user}
    return render(request, 'shop/signin.html', params)
