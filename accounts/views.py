from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import *
from .filters import OrderFilter
from .forms import CreateUserForm
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def dashboard(request):
    custs = Customer.objects.all()
    orders = Order.objects.all()    

    total_customers = custs.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'customers': custs, 'orders': orders, 'total_customers': total_customers,
               'total_orders': total_orders, 'delivered': delivered, 'pending': pending}
    return render(request, 'accounts/dashboard.html', context)


def about(request):
    return HttpResponse('<h2> About </h2>')


def products(request):
    prods = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': prods})


def customers(request, pk: int):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_filter = OrderFilter(request.GET, orders)
    orders = order_filter.qs

    context = {'customer': customer, 'orders': orders, 'order_filter': order_filter}
    return render(request, 'accounts/customers.html', context)


def create_order(request):
    form = OrderForm()
    context = {'form': form}
    if request.method == 'POST':
        # print(f"print Form : {request.POST}")
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    return render(request, 'accounts/create_order_form.html', context)


def update_order(request, pk: int):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {'form': form}
    return render(request, 'accounts/create_order_form.html', context)


def delete_order(request, pk: int):
    order = Order.objects.get(id=pk)
    context = {'order': order}
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    return render(request, 'accounts/delete_order_form.html', context)


def create_customer_order(request, cid: int):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=5)
    customer = Customer.objects.get(id=cid)
    formset = OrderFormSet(instance=customer, queryset=Order.objects.none())
    if request.method == 'POST':
        # print(f"print Form : {request.POST}")
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect(f"/customers/{customer.id}/")
    context = {'formset': formset, 'customer': customer}
    return render(request, 'accounts/inline_create_order_form.html', context)


def register(request):
    form = CreateUserForm()
    context = {'form': form}
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    return render(request, 'accounts/register.html', context)


def login(request):
    form = AuthenticationForm()
    context = {'form': form}
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            return redirect('home')
        else:
            print(form.errors)
    return render(request, 'accounts/login.html', context)
