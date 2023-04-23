from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.forms import forms
from .models import WatchModel, WatchRegistrationModel
from .forms import ContactForm, WatchregistrationForm, WatchBuyForm


# Create your views here.

class WatchView(ListView):
    model = WatchRegistrationModel
    template_name = "pages/index.html"
    context_object_name = 'watchs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['watchs_slide'] = WatchModel.objects.all().order_by('added_time')[3:6]
        context['all_watchs'] = WatchModel.objects.all().order_by('added_time')
        
        return context
    

class ContactView(CreateView):
    template_name = "pages/contact.html"

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            "form": form
        }
        return render(request, "pages/contact.html", context)
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == "POST" and form.is_valid():
            form.save()
            return redirect('home_page_view')
            # return HttpResponse("<h2>Malumotlaringiz muvaffaqiyatli junatildi!</h2>")

        context = {
            "form" : form
        }
        return render(request, "pages/contact.html", context)


class CreateWatchView(CreateView):
    model = WatchModel
    template_name = "pages/create_watch.html"
    fields = ['title', 'subtitle', 'price', 'about', 'image_one', 'image_two', 'image_three']
    success_url = reverse_lazy("home_page_view")


class DeleteWatchView(DeleteView):
    model = WatchModel
    context_object_name = 'detail'
    template_name = "pages/delete_watch.html"
    success_url = reverse_lazy("home_page_view")


class UpdateWatchView(UpdateView):
    model = WatchModel
    context_object_name = 'detail'
    template_name = "pages/update_watch.html"
    fields = ['title', 'subtitle', 'price', 'about', 'image_one', 'image_two', 'image_three']
    success_url = reverse_lazy("home_page_view")


class WatchDetail(DetailView):
    model = WatchModel
    template_name = "pages/watch_detail.html"
    context_object_name = "detail"


class WatchRegisterView(CreateView):
    template_name = "pages/watch_register.html"

    def get(self, request, pk):
        register_form = WatchregistrationForm()
        context = {
            "register_form" : register_form
        }
        return render(request, "pages/watch_register.html", context)
    
    def post(self, request, pk):
        register_form = WatchregistrationForm(request.POST)
        user = User(request.POST)
        watch = get_object_or_404(WatchModel, id=pk)
        if request.method == "POST" and register_form.is_valid():
            new_form = register_form.save(commit=False)
            new_form.user = request.user
            new_form.watch = watch
            new_form.save()
            return redirect('buy/')
        
        context = {
            "register_form" : register_form,
            "user" : user,
            "watch" : watch
        }
        return render(request, "pages/watch_register.html", context)


class WatchBuyView(CreateView):
    template_name = "pages/watch_buy.html"

    def get(self, request, pk):
        buy_form = WatchBuyForm()
        context = {
            "buy_form" : buy_form
        }
        return render(request, "pages/watch_buy.html", context)
    
    def post(self, request, pk):
        buy_form = WatchBuyForm(request.POST)
        watch_register = get_object_or_404(WatchRegistrationModel, pk=pk)
        if request.method == "POST" and buy_form.is_valid():
            new_buy_form = buy_form.save(commit=False)
            new_buy_form.registration = watch_register
            buy_form.save()
            return redirect('home_page_view')
        context = {
            "buy_form" : buy_form,
            "watch_register" : watch_register
        }
        return render(request, "pages/watch_buy.html", context)
