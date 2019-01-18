from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
@login_required
def forum_index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:







        return render(request, 'forum_index.html')