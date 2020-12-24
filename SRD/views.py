from django.shortcuts import render, redirect
from .models import *
from django.db.models import Sum
# Create your views here.

class SRDManagement():

    def SRD_home(self, request):
        """ SRD Home page """
        title = "Home"

        if not request.user.is_superuser:
            return redirect('index')

        purchases = Purchase.objects.all()
        items = Item.objects.all()
        items_amount = items.aggregate(Sum('purchase_cost'))

        context = {
            'title': title,
            'purchases': purchases,
            'items': items,
            'items_amount': items_amount,

        }

        return render(request, 'SRD/home.html', context)