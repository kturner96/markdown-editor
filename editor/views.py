
from django.shortcuts import get_object_or_404, render

from editor.models import Document


# Create your views here.
def editor(request, pk=None):
    if pk:
        document = get_object_or_404(Document, pk=pk, owner=request.user)
    else:
        document = None
    return render(request, 'editor/editor.html', {"document": document})
