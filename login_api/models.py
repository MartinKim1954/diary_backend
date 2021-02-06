from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=10, verbose_name='사용자 이름')
    email = models.EmailField(max_length=128, verbose_name='사용자 이메일')
    password = models.CharField(max_length=64, verbose_name='사용자 비밀번호')
    registered = models.DateTimeField(auto_now_add=True, verbose_name='사용자 가입날짜')

    # 별도로 테이블명을 지정하고 싶을 때 쓰는 코드(optional)
    class Meta:
        db_table = 'user'

class Feed(models.Model):
    user_id = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE ,verbose_name='특정 사용자')
    content = models.TextField(max_length=100, verbose_name='피드 내용')
    created = models.DateTimeField(auto_now_add=True, verbose_name='피드 생성날짜')

    class Meta:
        db_table = 'feed'