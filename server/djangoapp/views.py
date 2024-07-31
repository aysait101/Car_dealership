# Uncomment the required imports before adding the code

from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.views.decorators.csrf import csrf_exempt
import logging
import json

from .restapis import get_request, analyze_review_sentiments, post_review

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

# Create a `login_user` view to handle sign-in request
@csrf_exempt
def login_user(request):
    # Get username and password from request body
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    # Authenticate user
    user = authenticate(username=username, password=password)
    response_data = {"userName": username}
    if user is not None:
        # Login user
        login(request, user)
        response_data = {"userName": username, "status": "Authenticated"}
    return JsonResponse(response_data)


# Create a `logout_request` view to handle sign-out request
def logout_request(request):
    logout(request)
    return JsonResponse({"userName": ""})


# Create a `registration` view to handle sign-up request
@csrf_exempt
def registration(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']
    username_exists = False

    try:
        User.objects.get(username=username)
        username_exists = True
    except User.DoesNotExist:
        logger.debug(f"{username} is a new user")

    if not username_exists:
        # Create new user
        User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            email=email
        )
        # Login user
        login(request, User)
        response_data = {"userName": username, "status": "Authenticated"}
    else:
        response_data = {"userName": username, "error": "Already Registered"}
    
    return JsonResponse(response_data)


# Update the `get_dealership
