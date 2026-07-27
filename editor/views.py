from django.shortcuts import get_object_or_404, render
from .parser import parse_markdown

from editor.models import Document


# Create your views here.
def editor(request, pk=None):
    if pk:
        document = get_object_or_404(Document, pk=pk, owner=request.user)
        content = document.content
    else:
        document = None
        content = ''

    rendered_html = ''

    if request.method == 'POST':
        content = request.POST.get('content', '')
        rendered_html = parse_markdown(content)

    return render(request, 'editor/editor.html', {"document": document, "content": content, "rendered_html": rendered_html})
