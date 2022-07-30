from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SaleForm, CustomerDetailForm
from common.forms import AddressForm
from .models import Sale


def sale_list(request):

    sales = Sale.objects.filter(status = True).order_by('-date')
    context = {'sales':sales}
    return render(request, 'sale/list.html', context=context)

def add_sale(request):

    s_form = SaleForm()
    c_form = CustomerDetailForm()
    a_form = AddressForm()
    if request.method == "POST":
        s_form = SaleForm(request.POST)
        c_form = CustomerDetailForm(request.POST)
        a_form = AddressForm(request.POST)
        if s_form.is_valid() and c_form.is_valid() and a_form.is_valid():
            if request.POST.get('customer-skip'):
                customer = None
            else:
                address = a_form.save()
                customer = c_form.save(commit=False)
                customer.customer_address = address
                customer.save()
            sale = s_form.save(commit=False)
            sale.customer = customer
            sale.save()
            messages.success(request, 'Sale added successfully!')
            return redirect('sale:list')
        else:
            messages.error(request, str(s_form.errors) + str(c_form.errors) + str(a_form.errors))
    context = {'s_form':s_form, 'c_form':c_form, 'a_form':a_form}
    return render(request, 'sale/create.html', context=context)