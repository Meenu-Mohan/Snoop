from django.shortcuts import render, redirect
from home.models import Juvenile, Image
from django.contrib import messages
from addjuvenile.decorators import admin_required


@admin_required
def adminpanel(request):

    juvs = Juvenile.objects.order_by('id')
    return render(request, 'admin_panel.html',{'juvs':juvs})