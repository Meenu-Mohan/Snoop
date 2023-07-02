import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse 
from .face_recognition import run_face_recognition
from django.contrib import messages


def upload(request):
    return render(request, 'upload.html')

def process_image(request):
    if request.method == 'POST' and 'juvenile_img' in request.FILES:
        image_file = request.FILES['juvenile_img']
        image_path = os.path.join(settings.MEDIA_ROOT, 'processing', image_file.name)

        # Save the uploaded image temporarily
        with open(image_path, 'wb+') as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)

        # Run face recognition on the temporarily stored image
        known_face_found, recognized_faces = run_face_recognition(image_path)

        # Delete the temporarily stored image
        os.remove(image_path)

        if known_face_found == False:

            messages.success(request, f'The faces in the image was uknown!')

            return render(request, 'nomatchfound.html')
        else:
            # Pass the person_name to the template

            messages.success(request, f'The faces in the image was detected as {recognized_faces}!')

            return render(request, 'matchfound.html')

    return HttpResponse('Error: Invalid request')
