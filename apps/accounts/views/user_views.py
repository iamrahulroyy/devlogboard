from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def dashboard_view(request):
    user = request.user
    return JsonResponse({"message": f"Welcome, {user.username}!","email": user.email,})
