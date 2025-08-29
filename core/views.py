from django.shortcuts import render
from .models import MainUser
from django.db.models import Q

# Create your views here.
def home(request):
    query = request.GET.get('search', '')
    all_users = MainUser.objects.all()

    filtered_users = None

    if query:
        filtered_users = MainUser.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email__icontains=query) |
            Q(departamento__icontains=query)
        )

    return render(request, 'core/home.html', {
        'filtered_users': filtered_users, 
        'all_users': all_users,
        'query': query
    })