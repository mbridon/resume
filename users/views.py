from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect("experiencepro-list")

        return render(request, "login.html", {"form": form, "error": "Identifiants incorrects"})

    else:
        form = AuthenticationForm()

        return render(request, "login.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)

    return redirect(login_view)