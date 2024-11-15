from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required


@login_required()
def index(request):
    # @permission_required('shop.add_choice', login_url='logout')
    return render(request, 'main/index.html')