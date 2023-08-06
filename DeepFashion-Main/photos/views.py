from django.shortcuts import render, redirect
from .forms import PhotoForm
from .models import Photo


def photo_list(request):
    photos = Photo.objects.all()
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            new_photo = form.save(commit=False)
            new_photo.owner = request.user
            new_photo.save()
            return redirect("photos:photo_list")
    else:
        form = PhotoForm()
    return render(request, "photos/photo_list.html", {"photos": photos, "form": form})
