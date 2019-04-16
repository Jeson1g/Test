from django.shortcuts import render, redirect
from .models import Item, List


# Create your views here.
def home_page(request):
    """首页"""
    return render(request, 'home.html')


def view_list(request, list_id):
    """列表页"""
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {"list": list_})


def new_list(request):
    """创建新清单"""
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')


def add_item(request,  list_id):
    """添加新事项"""
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')



