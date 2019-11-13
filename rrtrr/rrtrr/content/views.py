# from .models import Contents
from django.shortcuts import render, get_object_or_404

# Create your views here.
def showtext(request):
    # content = get_object_or_404(Contents, pk=pk)
    content = '123'
    return render(request, 'content/show_content.html', {'content': content})
