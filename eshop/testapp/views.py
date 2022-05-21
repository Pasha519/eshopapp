from django.shortcuts import render,redirect
from testapp.models import Category,Products,Order
from testapp import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
# Create your views here.

#home view
def home_view(request):
    category = Category.objects.all()
    products = Products.objects.all()
    return render(request, 'testapp/index.html',{"categories":category,"products":products})

#categories and Items display view in home
def categoryListShow_View(request,id):
    category = Category.objects.all()
    products = Products.objects.filter(category=id)
    return render(request, 'testapp/index.html', {"categories": category, "products": products})


#item buy view
@login_required
def buy_view(request,id):
    products = Products.objects.get(id = id)
    #here product obj contain "name" field only.
    order = Order(product=products,customer=request.user,price=products.price)
    form = forms.OrderForm(instance=order)
    if request.method =="POST":
        form = forms.OrderForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Item Ordered Successfully.......!')
    return render(request, 'testapp/order.html',{"form":form})


#display ordered items
@login_required
def orderitems_view(request):
    orders = Order.objects.filter(customer__exact=request.user)
    return render(request, "testapp/orderdisp.html",{'orders':orders})

#delete ordered Items
@login_required
def orderdelete_view(request,price):
    orders = Order.objects.filter(customer__exact=request.user)
    orders1  =Order.objects.filter(price__exact = price)
    if orders1 is not None:
        orders1.delete()
        return redirect("/orderitems")
    return render(request, "testapp/orderdisp.html", {'orders': orders})

#signup form
def signup_view(request):
    form = forms.SignupForm()
    if request.method =="POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user=form.save()
            user.set_password(user.password)
            user.save()
        messages.success(request, "Signup Successfull...! login with username and password")
        subject = "Pasha Shopping Application"
        message = '''Welcome to Pasha Shopping Application,\nWe value our customers more than anything,and your satisfaction is what we aim for! Welcome to you!\nThank you for visiting us..........!\n
                                 \n\n\nThanks and Regards\nPasha Shopping Application Team'''
        from_email = "pashasoftsol@gmail.com"
        recipient_list = [email,]
        send_mail(subject, message, from_email, recipient_list)
    return render(request, 'testapp/signup.html',{"form":form})

#logout form
def logout_view(request):
    return render(request, 'testapp/logout.html')
