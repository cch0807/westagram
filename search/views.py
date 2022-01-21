import json

from django.http import JsonResponse
from django.views import View

from users.models import Users
# from postings.models import Search

# Create your views here.

class SearchView(View):
  def post(self, request):
    return JsonResponse({'message': 'SUCCESS'}, status=200)