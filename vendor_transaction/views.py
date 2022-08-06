from django.shortcuts import render, redirect, get_object_or_404
from vendor.models import Vendor
from .models import VendorTransaction
from .forms import VendorTransactionForm
from django.contrib import messages

# Create your views here.

def transactions_list(request, vendor_id):

    form = VendorTransactionForm()
    vendor = get_object_or_404(Vendor, id = vendor_id)
    transactions = VendorTransaction.objects.filter(
                    vendor__id = vendor_id).order_by('-date').all()

    [print(transaction.date) for transaction in transactions]
    
    context = {'transactions':transactions, 'form':form, 'vendor':vendor}
    return render(request, 'transaction/list.html', context=context)

def make_transaction(request, vendor_id):

    vendor = get_object_or_404(Vendor, id = vendor_id)
    if request.method == "POST":
        form = VendorTransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.vendor = vendor
            transaction.save()
            messages.success(request, 'Transaction successful!')
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, form.errors)
            return redirect(request.META.get('HTTP_REFERER'))