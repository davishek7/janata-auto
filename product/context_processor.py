from .forms import ProductCategoryForm


def product_context(request):
    return {
        'c_form' : ProductCategoryForm()
    }