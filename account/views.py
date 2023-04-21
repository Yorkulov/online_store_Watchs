from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import View
from django.urls import reverse_lazy,reverse
from django.contrib.auth import authenticate, login
from account.forms import UserRegistrationForm, LoginForm, UserEditForm

# Create your views here.

# def user_register(request):
#     if request.method == "POST":
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=False)
#             new_user.set_password(
#                 user_form.cleaned_data["password"]
#             )
#             new_user.save()
#             context = {
#                 "new_user" : new_user,
#             }
#             return HttpResponse("<h2>Success</h2>")
#             # return render(request, "pages/register.html", context)
#             # # return render(request, 'pages/register.html', context_instance=RequestContext(request))

#     else:
#         user_form = UserRegistrationForm()    
#     context = {
#         "user_form" : user_form,
#     }
#     return render(request, "pages/register.html", context)


def user_register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST) 
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data["password"]
            )
            new_user.save()
            # context = {
            #     "new_user" : new_user,
            # }
            # return render(request, 'pages/login.html', context)
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
        context = {
            "user_form" : user_form,
        }
        return render(request, 'pages/register.html', context)

class SignUpView(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    template_name = "pages/register.html"

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,
                                password=data['password'],
                                username=data['username'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("<h2>Success<h2>")
                else:
                    return HttpResponse("<h2>Profilingiz faol holatda emas</h2>")
            else:
                return HttpResponse("Login yoki parol xato")
    else:
        form = LoginForm()
        context = {
            "form" : form
        }
        return render(request, 'pages/login.html', context)
    

def profile(request):
    user_form = request.user
    context = {
        "user_form" : user_form
    }
    return render(request, "pages/profile.html", context)


class ProfileEdit(View):
    def get(self, request):
        user_form = UserEditForm(instance=request.user)
        context = {
            "user_form" : user_form
        }
        return render(request, "pages/profile_edit.html", context)

    def post(self, request):
        user_form = UserEditForm(instance=request.user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('home_page_view')
