from django.shortcuts import render
from django.utils import timezone
from .models import Item

# Create your views here.
def item_list(request):
    items = Item.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'item/item_list.html', {'items': items})

from django.shortcuts import render, get_object_or_404

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item/item_detail.html', {'item': item})