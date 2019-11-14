from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
from django.views import View
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from .forms import PostModelForm

from .models import Post

class ContentsListView(ListView):
    # queryset = Post.objects.all()
    template_name = 'contents/contents_list.html'
    def get_queryset(self):
        return Post.objects.all()

    # greeting = "good day"
    # posts = Post.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    #
    #
    # def get(self, request):
    #     return render(request, 'contents/contents_list.html', {'posts': self.posts})
    #


class ContentCreateView(View):
    template_name = 'contents/contents_create.html'
    def get(self, request, *args, **kwargs):
        form = PostModelForm()
        context = {"form":form}
        print(request)
        return render(request, self.template_name, context)
    def post(self, request,  *args, **kwargs):
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
        context = {"form":form}
        print(request.POST)
        print(request.FILES)
        return render(request, self.template_name, context)

class ContentsDetailView(DetailView):
    template_name = 'contents/contents_detail.html'
    queryset = Post.objects.all()
    context_object_name = 'abc'


    def get_object(self):
        id_= self.kwargs.get("id")
        # print(request)
        return get_object_or_404(Post, id=id_)


