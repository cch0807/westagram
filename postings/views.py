import json, bcrypt, jwt

from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError 

from users.models           import Users
from postings.models        import Post, Commit
from my_settings            import SECRET_KEY

class PostingView(View):
  def post(self,request):
    try:
      data = json.loads(request.body)
      if not Users.objects.filter(email = data['email']).exists():
        return JsonResponse({'message': 'INVALID_USER'}, status=400)
      
      Post.objects.create(
        user = Users.objects.get(email = data['email']),
        image = data["image"],
        post = data['post'],
      )
      return JsonResponse({'message': 'SUCCESS'}, status=200)
      
    except:
      return JsonResponse({"message": "KEY_ERROR"}, status=400)

  def get(self, request):
    try:
      result = []
      post = Post.objects.all()
      
      for ps in post:
        result.append({
          "name": ps.user.name,
          "image": ps.image,
          "post": ps.post,
          "time": ps.create_at,
        })

      return JsonResponse({'message': result}, status=200)

    except:
      return JsonResponse({'message': 'KEY_ERROR'}, status=400)

class CommitView(View):
  def post(self, request):
    try:
      data = json.loads(request.body)
      if not Users.objects.filter(email=data['email']).exists():
        return JsonResponse({'message': 'INVALID_USER'}, status= 400)

      if not Post.objects.filter(id = data['post_id']).exists(): 
        return JsonResponse({'message': 'NO_POST'}, status=400)

      Commit.objects.create(
        user = Users.objects.get(email = data['email']),
        post_id = data['post_id'],
        comment = data['comment']
      )
      return JsonResponse({'message': 'SUCCESS'}, status=200)

    except:
      return JsonResponse({"message": "KEY_ERROR"}, status=400)
  
  def get(self, request,post_id):
    try:

      # data = json.loads(request.body)
      # user = Commit.objects.get(user_id = data['user_id'])
   
      comments = Commit.objects.filter(post_id= post_id)
      result = []

      for comment in comments:
        result.append(
          {
            "user_id": comment.user.name,
            "comment": comment.comment,
            "time":    comment.create_at
          }
        )
      return JsonResponse({'result':result}, status=200)
    except:
      return JsonResponse({'message': 'KEY_ERROR'}, status=400)
