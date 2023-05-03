from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from .models import Ad, Comments
from .filters import AdFilter, AdCommentsFilter
from .forms import AdForm, CommentForm


class AdList(ListView):
    model = Ad
    ordering = '-id'
    template_name = 'ad.html'
    context_object_name = 'ad'
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AdFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class AdDetail(FormMixin, DetailView):
    model = Ad
    template_name = 'post.html'
    context_object_name = 'post'
    form_class = CommentForm
    success_msg = 'Комментарий создан'

    def get_success_url(self):
        return reverse_lazy('ad_detail', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.ad = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class AdCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = AdForm
    model = Ad
    template_name = 'ad_edit.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class AdUpdate(LoginRequiredMixin, UpdateView):
    form_class = AdForm
    model = Ad
    template_name = 'ad_edit.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs


class AdDelete(LoginRequiredMixin, DeleteView):
    model = Ad
    template_name = 'ad_delete.html'
    success_url = reverse_lazy('ad')


class UserPostCommentList(LoginRequiredMixin, generic.ListView):
    raise_exception = True
    model = Comments
    template_name = 'user_posts_comments.html'
    context_object_name = 'user_posts_comments'
    paginate_by = 3

    def get_queryset(self):
        queryset = Comments.objects.filter(ad__author=self.request.user).all()
        return queryset

    def get_queryset(self):
        queryset = Comments.objects.filter(ad__author=self.request.user).order_by('-time_in').all()
        self.filterset = AdCommentsFilter(self.request.GET, queryset)
        self.filterset.form.fields['ad'].queryset = Ad.objects.filter(author=self.request.user)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


@login_required
def comments_accept(request, **kwargs):
    response = Comments.objects.get(id=kwargs.get('pk'))
    response.status = True
    response.save()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def comments_delete(request, **kwargs):
    response = Comments.objects.get(id=kwargs.get('pk'))
    response.delete()
    return redirect(request.META.get('HTTP_REFERER'))



