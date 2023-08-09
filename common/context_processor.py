from .forms import SearchForm


def common_context(request):

    return {
        'search_form': SearchForm()
    }
