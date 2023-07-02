from django.shortcuts import render, redirect
from home.models import Juvenile, Image
from django.contrib import messages
from .decorators import admin_required
from .tasks import process_juvenile_records

@admin_required
def add_juvenile(request):
    if request.method == 'POST':
        name = request.POST['name']
        sex = request.POST['sex']
        age = request.POST['age']
        dob = request.POST['dob']
        weight = request.POST['weight']
        height = request.POST['height']
        address = request.POST['address']
        juvenile_img = request.FILES['juvenile_img']
        more_images = request.FILES.getlist('more_img')

        juvenile = Juvenile(
            name=name, sex=sex, age=age, dob=dob, weight=weight, height=height, address=address, juvenile_img=juvenile_img
        )
        juvenile.save()

        for img in more_images:
            if img:
                Image.objects.create(image=img, juvenile=juvenile)

        messages.success(request, 'Juvenile Record added successfully!')

        train_dir = "F:/CLIFFIN/FINAL/snoop/media/juveniles/"
        process_juvenile_records.delay(train_dir)

        return redirect('addjuvenile:add_juvenile')
    else:
        return render(request, 'addjuvenile.html')
