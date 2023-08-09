from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import BatteryWarrantyClaim
from .forms import WarrantyClaimCreateForm
from common.forms import AddressForm
from sale.forms import CustomerDetailForm
from common.models import Address
from sale.models import CustomerDetail

# Create your views here.


def claims_list(request):

    claims = BatteryWarrantyClaim.objects.filter(
        status=True).order_by('-receive_date').all()
    context = {'claims': claims}
    return render(request, 'service/warranty-claim/list.html', context=context)


def add_claim(request):

    w_form = WarrantyClaimCreateForm()
    c_form = CustomerDetailForm()
    a_form = AddressForm()
    if request.method == "POST":
        a_form = AddressForm(request.POST)
        c_form = CustomerDetailForm(request.POST)
        w_form = WarrantyClaimCreateForm(request.POST)
        if a_form.is_valid() and c_form.is_valid() and w_form.is_valid():
            address = a_form.save()
            customer = c_form.save(commit=False)
            customer.address = address
            customer.save()
            claim = w_form.save(commit=False)
            claim.customer = customer
            claim.save()
            messages.success(request, 'Claim added successfully!')
            return redirect('service:list')
        else:
            messages.success(request, str(w_form.errors) +
                             str(c_form.errors) + str(a_form.errors))
    context = {'w_form': w_form, 'c_form': c_form, 'a_form': a_form}
    return render(request, 'service/warranty-claim/create.html', context=context)


def update_claim(request, pk):

    claim = get_object_or_404(BatteryWarrantyClaim, id=pk)
    customer = get_object_or_404(CustomerDetail, id=claim.customer.id)
    address = get_object_or_404(Address, id=customer.address.id)
    w_form = WarrantyClaimCreateForm(instance=claim)
    c_form = CustomerDetailForm(instance=customer)
    a_form = AddressForm(instance=address)
    if request.method == "POST":
        a_form = AddressForm(request.POST, instance=address)
        c_form = CustomerDetailForm(request.POST, instance=customer)
        w_form = WarrantyClaimCreateForm(request.POST, instance=claim)
        if a_form.is_valid() and c_form.is_valid() and w_form.is_valid():
            a_form.save()
            customer.save()
            claim.save()
            messages.success(request, 'Claim updated successfully!')
            return redirect('service:list')
        else:
            messages.success(request, str(w_form.errors) +
                             str(c_form.errors) + str(a_form.errors))
    context = {'claim': claim, 'w_form': w_form,
               'c_form': c_form, 'a_form': a_form}
    return render(request, 'service/warranty-claim/update.html', context=context)
