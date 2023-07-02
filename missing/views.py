from django.shortcuts import render, get_object_or_404, redirect
from home.models import Juvenile
from datetime import date

def missing(request):
    juvs = Juvenile.objects.order_by('-id')
    return render(request, 'juveniles.html', {'juvs': juvs})

def juvenile_details(request, id):
    juvenile = get_object_or_404(Juvenile, id=id)

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'set_found':
            juvenile.missing = False
            juvenile.missing_date = None
        elif action == 'set_missing':
            juvenile.missing = True
            juvenile.missing_date = date.today()
        elif action == 'delete_record':
            # Delete associated Image objects
            images = juvenile.more_images.all()
            for image in images:
                image.image.delete()
                image.delete()

            juvenile.juvenile_img.delete()
            # Delete record logic here
            juvenile.delete()
            return redirect('adminpanel:adminpanel')  # Redirect to missing page after deletion
        elif action == 'upload_snoop':
            return redirect('upload:upload')

        juvenile.save()

    return render(request, 'detail.html', {'juvenile': juvenile})

def set_missing(request, id):
    if request.method == 'POST':
        juvenile = get_object_or_404(Juvenile, id=id)
        juvenile.missing = True
        juvenile.missing_date = date.today()
        juvenile.save()
    return redirect('missing:juvenile_details', id=id)  # Redirect back to the same juvenile detail page

def set_found(request, id):
    if request.method == 'POST':
        juvenile = get_object_or_404(Juvenile, id=id)
        juvenile.missing = False
        juvenile.missing_date = None
        juvenile.save()
    return redirect('missing:juvenile_details', id=id)  # Redirect back to the same juvenile detail page

def delete_record(request, id):
    if request.method == 'POST':
        print(f"Deleting record with ID: {id}")
        juvenile = get_object_or_404(Juvenile, id=id)

        # Delete associated Image objects
        images = juvenile.more_images.all()
        for image in images:
            image.image.delete()
            image.delete()

        # Delete the Juvenile object
        juvenile.juvenile_img.delete()
        juvenile.delete()

    return redirect('adminpanel:adminpanel')  # Redirect to missing page after deletion

def upload_snoop(request):
    if request.method == 'POST':
        return redirect('upload:upload')
