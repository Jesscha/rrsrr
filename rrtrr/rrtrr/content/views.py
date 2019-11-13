from .models import Contents
from django.shortcuts import render, get_object_or_404

# Create your views here.
def showtext(request, pk):
    content = get_object_or_404(Contents, pk=pk)
    return render(request, 'templates/content/show_content.html', {'content': content})
