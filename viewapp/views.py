from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.forms import forms
from hitcount.models import HitCount
from hitcount.views import HitCountMixin, get_hitcount_model
from .models import WatchModel, WatchRegistrationModel
from .forms import WatchregistrationForm, WatchBuyForm
from account.forms import CommentForm
from account.models import CommentModel


# Create your views here.

class WatchView(ListView):
    model = WatchRegistrationModel
    template_name = "pages/index.html"
    context_object_name = 'watchs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['watchs_slide'] = WatchModel.objects.all().order_by('added_time')[
            3:6]
        context['all_watchs'] = WatchModel.objects.all().order_by('added_time')

        return context


class CreateWatchView(LoginRequiredMixin, CreateView):
    model = WatchModel
    template_name = "pages/create_watch.html"
    fields = ['title', 'title_uz', 'title_en', 'title_ru', 'subtitle', 'subtitle_uz', 'subtitle_en', 
              'subtitle_ru', 'price', 'about', 'about_uz', 'about_en', 'about_ru',
              'image_one', 'image_two', 'image_three']
    success_url = reverse_lazy("home_page_view")


class DeleteWatchView(LoginRequiredMixin, DeleteView):
    model = WatchModel
    context_object_name = 'detail'
    template_name = "pages/delete_watch.html"
    success_url = reverse_lazy("home_page_view")


class UpdateWatchView(LoginRequiredMixin, UpdateView):
    model = WatchModel
    context_object_name = 'detail'
    template_name = "pages/update_watch.html"
    fields = ['title', 'subtitle', 'price', 'about',
              'image_one', 'image_two', 'image_three']
    success_url = reverse_lazy("home_page_view")


class WatchRegisterView(LoginRequiredMixin, CreateView):
    template_name = "pages/watch_register.html"

    def get(self, request, pk):
        register_form = WatchregistrationForm()
        context = {
            "register_form": register_form
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
            "register_form": register_form,
            "user": user,
            "watch": watch
        }
        return render(request, "pages/watch_register.html", context)


class WatchBuyView(LoginRequiredMixin, CreateView):
    template_name = "pages/watch_buy.html"

    def get(self, request, pk):
        buy_form = WatchBuyForm()
        context = {
            "buy_form": buy_form
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
            "buy_form": buy_form,
            "watch_register": watch_register
        }
        return render(request, "pages/watch_buy.html", context)


class CommentView(HitCountMixin, CreateView, ListView):
    model = CommentModel
    context_object_name = "comments"
    success_url = reverse_lazy('watch_detail, watch.pk')

    def get(self, request, pk):
        form = CommentForm(request.POST)
        context = {
            "form": form
        }
        return render(request, "pages/comment.html", context)

    def post(self, request, pk):
        if request.method == "POST":
            form = CommentForm(request.POST)
            user = request.user
            watch = WatchModel(pk=pk)
            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.user = user
                new_form.watch = watch
                form.save()
                form = CommentForm()
            context = {
                "form": form,
                "user": user,
                "watch": watch,
                "new_form": new_form
            }
            return render(request, "pages/comment.html", context)


def watchDetail(request, pk):
    detail = get_object_or_404(WatchModel, pk=pk)
    context = {}
    hit_count = get_hitcount_model().objects.get_for_object(detail)
    hits = hit_count.hits
    hitcontext = context['hitcount'] = {'pk' : hit_count.pk}
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    if hit_count_response.hit_counted:
        hits = hits + 1
        hitcontext['hit_counted'] = hit_count_response.hit_counted
        hitcontext['hit_message'] = hit_count_response.hit_message
        hitcontext['total_hits'] = hits

    comments = detail.comments.filter(active=True)
    detail.view_count = detail.view_count + 1
    detail.save()
    new_comment = None
    comment_count = comments.count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.watch = detail
            new_comment.user = request.user
            new_comment.save()
            # comment_form.save()
            comment_form = CommentForm()

    else:
        comment_form = CommentForm()

    context = {
        "detail" : detail,
        "comments" : comments,
        "new_comment" : new_comment,
        "comment_form" : comment_form,
        "comment_count" : comment_count
    }

    return render(request, "pages/watch_detail.html", context)

