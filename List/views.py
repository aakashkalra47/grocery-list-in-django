from django.shortcuts import render,redirect
from List.models import Item
from List.forms import ItemForm
def home(request):
    filterDate=request.GET.get('filterDate','')
    if(filterDate==''):
        items=Item.objects.all()
    else:
        items=Item.objects.all().filter(date=filterDate)
    data={
        'items':items,
        'filter':filterDate
    }
    return render(request,'List/index.html', data);
def addItem(request):
    if request.method=="POST":
        form=ItemForm(request.POST)
        if form.is_valid():
            item=Item()
            item.name=form.cleaned_data['item_name']
            item.quantity=form.cleaned_data['item_quantity']
            item.status=form.cleaned_data['item_status']
            item.date=form.cleaned_data['addedAt']
            item.save()
        return redirect('/')
    else:
        return render(request,'List/add.html')
def deleteItem(request,itemId):
    Item.objects.filter(id=itemId).delete()
    return redirect('/')
def updateItem(request,itemId):
    if request.method=="POST":
        form=ItemForm(request.POST)
        if form.is_valid():
            item=Item()
            item.name=form.cleaned_data['item_name']
            item.quantity=form.cleaned_data['item_quantity']
            item.status=form.cleaned_data['item_status']
            item.date=form.cleaned_data['addedAt']
            item.id=itemId
            item.save()
        return redirect('/')
    else:
        item=Item.objects.get(id=itemId)
        data={
            'item':item
        }
        return render(request,'List/update.html',data);