
from django.http import HttpResponse
from django.shortcuts import render, redirect

from lists.models import Item
# Create your views here.
def home_page(request):
    items = Item.objects.all()
    return render(request, 'home.html',{'items': items})


def list_view(request):    
    items = Item.objects.all()
    return render(request, 'list.html',{'items': items})

def new_list(request):
    new_item_text = request.POST['item_text']
    Item.objects.create(text=new_item_text)  

    return redirect('/lists/the-only-list-in-the-world/')