from curses import keyname
import json, bcrypt, jwt

from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError 
from django.db.models       import Q

from users.models           import Users
from postings.models        import Post, Comment, Like, Follow

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
          'id': ps.id,
          "name": ps.user.name,
          "image": ps.image,
          "post": ps.post,
          "time": ps.create_at,
        })

      return JsonResponse({'result': result}, status=200)

    except:
      return JsonResponse({'message': 'KEY_ERROR'}, status=400)

class CommentView(View):
  def post(self, request,post_id):
    try:
      data = json.loads(request.body)
      if not Users.objects.filter(email=data['email']).exists():
        return JsonResponse({'message': 'INVALID_USER'}, status= 400)

      if not Post.objects.filter(id = data['post_id']).exists(): 
        return JsonResponse({'message': 'NO_POST'}, status=400)

      Comment.objects.create(
        user = Users.objects.get(email = data['email']),
        post_id = data['post_id'],
        comment = data['comment'],
      )
      return JsonResponse({'message': 'SUCCESS'}, status=200)

    except:
      return JsonResponse({"message": "KEY_ERROR"}, status=400)
  
  def get(self, request, post_id):
    try:

      # data = json.loads(request.body)
      # user = Commit.objects.get(user_id = data['user_id'])
   
      comments = Comment.objects.filter(post_id= post_id)
      result = []

      for comment in comments:
        result.append(
          {
            'id': comment.id,
            "name": comment.user.name,
            "comment": comment.comment,
            "time":  comment.create_at
          }
        )
      return JsonResponse({'result':result}, status=200)
    except:
      return JsonResponse({'message': 'KEY_ERROR'}, status=400)
      
class LikeView(View):
  def post (self,request):
    data = json.loads(request.body)

    if not Users.objects.filter(email=data['email']).exists():
      return JsonResponse({'message': 'INVALID_USER'}, status= 400)

    if not Post.objects.filter(id = data['post_id']).exists():
      return JsonResponse({'message': 'NO_POST'}, status=400)

    like, is_like = Like.objects.get_or_create(
      user_id = Users.objects.get(email = data['email']).id,
      post_id = data['post_id']
    )

    if not is_like:
      like.delete()
      return JsonResponse({"message":"DELETE"}, status=200)
    
    # user = Users.objects.get(user_id = data['user_id'])
    # post = Post.objects.get(post_id = data['post_id'])

    try:
      return JsonResponse({'message': 'SUCCESS'}, status=200)
    except:
      return JsonResponse({'message': 'KEY_ERROR'}, status=400)

class FollowView(View):
  def post(self,request):
    try:
      data= json.loads(request.body)
      
      if not Users.objects.filter(email=data['follow_email']).exists():
        return JsonResponse({'message': 'INVALID_FOLLOW_USER'}, status=400)
      if not Users.objects.filter(email=data['followed_email']).exists():
        return JsonResponse({'message': 'INVALID_FOLLOWED_USER'}, status=400)
    
      follow, is_follow = Follow.objects.get_or_create(
        follow_user_id = Users.objects.get(email=data['follow_email']).id,
        followed_user_id = Users.objects.get(email=data['followed_email']).id
      )

      if not is_follow:
        follow.delete()
        return JsonResponse({'message':'DELETE'}, status=200)

      return JsonResponse({'message': 'SUCCESS'}, status=200)
      
    except:
      return JsonResponse({'message': 'KEY_ERROR'}, status=400)

class CountView(View):
  def get(self,request,post_id):

    try:
      if not Post.objects.filter(id = post_id).exists():
        return JsonResponse({'message': 'INVALID_POST'}, status=400)
        
      count = Like.objects.filter(post_id = post_id).count()

      return JsonResponse({'like_count': count}, status=200)
    
    except:
      return JsonResponse({'message': 'KEY_ERROR'}, status=400)

class SearchView(View):
  def post(self,request):
    try:
      data = json.loads(request.body)
      # users = Users.objects.all()
      key = data['search']
      name_q = Q(name__contains = key)
      result = []
      users = Users.objects.filter(name_q)
      for user in users:
        result.append(user.name)

      return JsonResponse({'result': result}, status=200)

    except:
      return JsonResponse({'message': 'KEY_ERROR'}, status = 400)


class MainView(View):
  def get(self, request):
    try:
      user_list= []
      post_list = []
      comment_list = []
      like_list = []
      follow_list = []

      users = Users.objects.all()
      posts = Post.objects.all()
      comments = Comment.objects.all()
      likes = Like.objects.all()
      follows = Follow.objects.all()

      for user in users:
        user_list.append({
          'id':user.id,
          'name':user.name
          })

      for post in posts:
        post_list.append({
          'id': post.id,
          'image': post.image,
          'post': post.post
        })
      for comment in comments:
        comment_list.append({
          'id': comment.id,
          "name": comment.user.name,
          "comment": comment.comment,
          "time":  comment.create_at
        })
      
      for like in likes:
        like_list.append({
          'like_id' :like.id,
          'user_id' :like.user.id,
          'post_id' :like.post.id,
        })

      # for follow in follows:
      #   follow_list.append({

      #   })
      

      

      return JsonResponse({'user': user_list, 'post': post_list ,'comment': comment_list, 'like': like_list})

    except:

      return JsonResponse({'message': 'KEY_ERROR'})