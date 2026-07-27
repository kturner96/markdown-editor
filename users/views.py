
from django.contrib.auth import login
from django.shortcuts import redirect, render

from editor.models import Document

from .forms import StyledAuthenticationForm, StyledUserCreationForm

# Create your views here.

def auth_view(request):
    login_form = StyledAuthenticationForm()
    register_form = StyledUserCreationForm()

    if request.user.is_authenticated:
        return redirect("editor")

    if request.method == 'POST':  # noqa: SIM102
        if 'login_form' in request.POST:
            login_form = StyledAuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('editor_new')
        elif 'register_form' in request.POST:
                register_form = StyledUserCreationForm(request.POST)
                if register_form.is_valid():
                    user = register_form.save()
                    login(request, user)
                    return redirect('editor_new')

    return render(request, 'users/login.html', {
        'login_form': login_form,
        'register_form': register_form,
    })

def profile(request):
    documents = Document.objects.order_by("-updated_at")[:5]
    context = {"documents": documents}
    return render(request, 'users/profile.html', context)
