from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Vendor, Address
from .forms import VendorForm
from common.forms import AddressForm

# Create your views here.

def vendor_list(request):
    vendors = Vendor.objects.filter(status=True)
    context = {'vendors':vendors}
    return render(request, 'vendor/list.html', context=context)

def add_vendor(request):
    v_form = VendorForm()
    a_form = AddressForm()
    if request.method == "POST":
        v_form = VendorForm(request.POST)
        a_form = AddressForm(request.POST)
        if v_form.is_valid() and a_form.is_valid():
            address = a_form.save()
            vendor = v_form.save(commit=False)
            vendor.address = address
            vendor.save()
            messages.success(request, 'Vendor added successfully!')
            if request.POST.get('save-list'):
                return redirect('vendor:list')
            elif request.POST.get('save-add'):
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, str(v_form.errors)+str(a_form.errors))
            return redirect(request.META.get('HTTP_REFERER'))
    context = {'v_form':v_form, 'a_form':a_form}
    return render(request, 'vendor/create.html', context=context)

def update_vendor(request, pk):
    vendor = get_object_or_404(Vendor, id=pk)
    address = get_object_or_404(Address, id=vendor.address.id)
    v_form = VendorForm(instance=vendor)
    a_form = AddressForm(instance=address)
    if request.method == "POST":
        v_form = VendorForm(request.POST, instance=vendor)
        a_form = AddressForm(request.POST, instance=address)
        if v_form.is_valid() and a_form.is_valid():
            a_form.save()
            v_form.save()
            messages.success(request, 'Vendor updated successfully!')
            return redirect('vendor:list')
        else:
            messages.error(request, str(v_form.errors)+str(a_form.errors))
            return redirect(request.META.get('HTTP_REFERER'))
    context = {'v_form':v_form, 'a_form':a_form, 'vendor':vendor}
    return render(request, 'vendor/update.html', context=context)


def delete(request):
    pass
