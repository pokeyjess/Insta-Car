from django.shortcuts import render, HttpResponseRedirect, reverse
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth import login, logout, authenticate
from insta_user.models import InstaUser
from authentication.forms import SignUpForm, LoginForm



def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST,request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            new_user = InstaUser.objects.create_user(username=data.get("username"), password=data.get("password"), bio=data.get("bio"), website=data.get("website"), profile_image=data.get("profile_image"))
            login(request, new_user)
            return HttpResponseRedirect(reverse("homepage"))  
        else:
            return HttpResponse(form.errors.values())
    form = SignUpForm()
    return render(request, 'generic_form.html', {"form": form})
  
class LoginView(TemplateView):
  
    def get(self, request):
        form = LoginForm()
        return render(request, "generic_form.html", {"form": form})

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
                data = form.cleaned_data
                user = authenticate(request, username=data.get("username"), password=data.get("password"))
                if user:
                    login(request, user)
                    return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))
                else:
                     return render(request, "generic_form.html", {"form": form})
                       

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))

