from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from common.models import Address
from ..models import BatterySale, CustomerDetail
from ..forms import BatterySaleForm, CustomerDetailForm, BatterySaleUpdateForm
from common.forms import AddressForm


def battery_sale_list(request):

    battery_sales = BatterySale.objects.filter(status = True).order_by('-date').all()
    context = {'battery_sales':battery_sales}
    return render(request, 'sale/battery/list.html', context=context)

def add_battery_sale(request):

    b_form = BatterySaleForm(initial={'discount':0})
    c_form = CustomerDetailForm()
    a_form = AddressForm()
    if request.method == "POST":
        b_form = BatterySaleForm(request.POST)
        c_form = CustomerDetailForm(request.POST)
        a_form = AddressForm(request.POST)
        if b_form.is_valid() and c_form.is_valid() and a_form.is_valid():
            address = a_form.save()
            customer = c_form.save(commit=False)
            customer.address = address
            customer.save()
            battery = b_form.save(commit=False)
            battery.customer = customer
            battery.save()
            messages.success(request, 'Battery sale added successfully!')
            return redirect('sale:battery_sale_list') 
        else:
            messages.error(request, str(b_form.errors) + str(c_form.errors) + str(a_form.errors))
    context = {'b_form':b_form, 'c_form':c_form, 'a_form':a_form}
    return render(request, 'sale/battery/create.html', context=context)

def update_battery_sale(request, pk):

    battery_sale = get_object_or_404(BatterySale, id=pk)
    customer = get_object_or_404(CustomerDetail, id=battery_sale.customer.id)
    address = get_object_or_404(Address, id=customer.address.id)
    b_form = BatterySaleUpdateForm(instance=battery_sale)
    c_form = CustomerDetailForm(instance=customer)
    a_form = AddressForm(instance=address)
    if request.method == "POST":
        b_form = BatterySaleUpdateForm(request.POST, instance=battery_sale)
        c_form = CustomerDetailForm(request.POST, instance=customer)
        a_form = AddressForm(request.POST, instance=address)
        if b_form.is_valid() and c_form.is_valid() and a_form.is_valid():
            a_form.save()
            c_form.save()
            b_form.save()
            messages.success(request, 'Battery sale updated successfully!')
            return redirect('sale:battery_sale_list') 
        else:
            messages.error(request, str(b_form.errors) + str(c_form.errors) + str(a_form.errors))
    context = {'b_form':b_form, 'c_form':c_form, 'a_form':a_form, 'battery_sale':battery_sale}
    return render(request, 'sale/battery/update.html', context=context)