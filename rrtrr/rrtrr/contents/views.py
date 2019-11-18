import datetime

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
from .forms import PostModelForm, RawPostModelForm

from .models import Post


class ContentsHomeView(ListView):
    # queryset = Post.objects.all()
    template_name = 'contents/contents_home.html'
    def get_queryset(self):
        return Post.objects.all()

class ContentsListView(ListView):
    # queryset = Post.objects.all()
    template_name = 'contents/contents_list.html'
    def get_queryset(self):
        return Post.objects.all()

#
# class ContentCreateView(View):
#     template_name = 'contents/contents_create.html'
#
#     def get(self, request):
#         my_form = RawPostModelForm()
#         context = {
#             "form": my_form
#         }
#         return render(request, self.template_name, context)
#
#     def post(self, request):
#         my_form = RawPostModelForm(request.POST)
#
#         if my_form.is_valid():
#             Post.objects.create(**my_form.cleaned_data)
#         context = {
#             "form": my_form
#         }
#
#         return render(request, self.template_name, context)





#  modelform
class ContentCreateView(View):
    template_name = 'contents/contents_create.html'

    def get(self, request, *args, **kwargs):
        proposed_renewal_date = datetime.date.today()
        form = PostModelForm(initial={'pub_date': proposed_renewal_date})
        context = {"form":form}

        return render(request, self.template_name, context)
    def post(self, request,  *args, **kwargs):
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        context = {"form":form}
        return render(request, self.template_name, context)

class ContentsDetailView(DetailView):
    template_name = 'contents/contents_detail.html'
    queryset = Post.objects.all()
    context_object_name = 'abc'


    def get_object(self):
        id_= self.kwargs.get("id")
        # print(request)
        return get_object_or_404(Post, id=id_)


