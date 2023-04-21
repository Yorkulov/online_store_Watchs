from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.forms import forms
from .models import WatchModel
from .forms import ContactForm


# Create your views here.

class WatchView(ListView):
    model = WatchModel
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
            return HttpResponse("<h2>Malumotlaringiz muvaffaqiyatli junatildi!</h2>")

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


    
