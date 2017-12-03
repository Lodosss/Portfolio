from django.shortcuts import render
from .forms import SubscruberForm
# Create your views here.
def post_list(request):
    form = SubscruberForm(request.POST or None)
    return render(request, 'landing/index.html', {})