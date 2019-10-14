from django.shortcuts import render
from .models import Post
# Create your views here.
def post_list(request):
    return render(request, 'VentasTopanzi/index.html', {})
