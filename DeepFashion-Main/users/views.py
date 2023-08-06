from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect(reverse("photos:photo_list"))
        else:
            # Return an 'invalid login' error message.
            return render(
                request, "users/login.html", {"error": "Invalid username or password"}
            )
    else:
        return render(request, "users/login.html")
