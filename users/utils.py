import jwt

from django.http import JsonResponse

from my_settings import SECRET_KEY, ALGORITHM
from users.models import Users

def login_required(func):
  def wrapper(self, request, *args, **kwargs):
    try:
      token = request.headers.get("Authorization", None)
      payload = jwt.decode(token, SECRET_KEY, algorithm=ALGORITHM)
      user = Users.objects.get(id=payload["id"])
      request.user = user

    except jwt.exceptions.DecodeError:
      return JsonResponse({'message': 'INVALID_TOKEN'}, status=400)

    except Users.DoesNotExist:
      return JsonResponse({'message': 'INVALID_USER'}, status= 400)
    return func(self, request, *args, **kwargs)
  return wrapper