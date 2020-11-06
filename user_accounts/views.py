from django.shortcuts import render
from user_accounts.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
        ]


class LoginView(auth_views.LoginView):
    template_name = "login.html"
    form_class = AuthenticationForm

    def get_success_url(self):
        return reverse("index")


def sign_in(request):
    context = {}
    form = AuthenticationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            login(request, form.get_user())
            return render(request, "index.html")
    context["form"] = form
    return render(request, "login.html", context)


def sign_up(request):
    context = {}
    form = CustomUserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, "index.html")
    context["form"] = form
    return render(request, "register.html", context)


def user_list(request):
    users = User.objects.all()
    return render(request, "base.html", {"users": users})


@login_required
def user_update(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, "base.html", {"user": user})


@login_required
def user_delete(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, "base.html", {"user": user})
