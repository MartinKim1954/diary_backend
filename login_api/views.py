from django.http.response import JsonResponse
from django.views.decorators import csrf
from rest_framework import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User, Feed
from .serializers import UserSerializer, FeedSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def helloAPI(request):
    return Response("Hello World!")

@api_view(['GET', 'POST', 'DELETE'])
def sign_up(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'success': True}, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'POST', 'DELETE'])
def show_users(request):
    if request.method == "GET":
        query_set = User.objects.all()
        serializer = UserSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def log_in(request):
    if request.method == "POST":
        input_user = JSONParser().parse(request)

        # email에 매칭되는 유저가 없을때
        try:
            db_user = User.objects.get(email=input_user.get('email'))
        except:
            return JsonResponse({'success': False}, safe=False)

        # 비번이 틀렸을 경우
        if db_user.password != input_user.get('password'):
            return JsonResponse({'success': False}, safe=False)

        # 로그인 성공
        if db_user.password == input_user.get('password'):
            # user_id 넘어가는지만 보면 될 듯?
            return JsonResponse({'success': True, 'user_id': db_user.id}, safe=False)

@api_view(['GET', 'POST'])
def get_feeds(request):
    if request.method == "POST":
        input_user = JSONParser().parse(request)
        query_set = Feed.objects.filter(user_id=input_user.get('user_id'))
        serializer = FeedSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def post_feed(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = FeedSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'success': True}, status=201)
        return JsonResponse(serializer.errors, status=400)