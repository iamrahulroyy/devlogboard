from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

@csrf_exempt
@require_http_methods(["GET", "POST"])
def signup_view(request):
    if request.method == "GET":
        return JsonResponse({"message": "Signup endpoint is working."})

    try:
        data = json.loads(request.body)
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if not all([username, email, password]):
            return JsonResponse({"error": "All fields are required."}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already exists."}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password)
        return JsonResponse({"message": "User created successfully."}, status=201)

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON."}, status=400)


@csrf_exempt
@require_http_methods(["GET", "POST"])
def login_view(request):
    if request.method == "GET":
        return JsonResponse({"message": "Login endpoint is working."})

    try:
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"message": "Login successful."})
        else:
            return JsonResponse({"error": "Invalid credentials."}, status=401)

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON."}, status=400)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def logout_view(request):
    if request.method == "GET":
        return JsonResponse({"message": "Logout endpoint is working."})

    if request.user.is_authenticated:
        logout(request)
        return JsonResponse({"message": "Logout successful."})
    else:
        return JsonResponse({"error": "User not logged in."}, status=401)

