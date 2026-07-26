
from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import StyledAuthenticationForm, StyledUserCreationForm

# Create your views here.

def auth_view(request):
    login_form = StyledAuthenticationForm()
    register_form = StyledUserCreationForm()

    if request.method == 'POST':  # noqa: SIM102
        if 'login_form' in request.POST:
            login_form = StyledAuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('editor')
        elif 'register_form' in request.POST:
                register_form = StyledUserCreationForm(request.POST)
                if register_form.is_valid():
                    user = register_form.save()
                    login(request, user)
                    return redirect('editor')

    return render(request, 'auth/login.html', {
        'login_form': login_form,
        'register_form': register_form,
    })
