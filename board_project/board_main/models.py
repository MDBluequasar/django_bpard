from django.db import models



# Create your models here.
# models.py의 class와 DB의 table과 sync를 맞춰 table(column 정보) 자동생성.

# class name 이 table명, 변수는 column명

class Test(models.Model): 
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)

class Author(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    # DB 설정에 default timestamp가 걸리는 것이 아닌, 장고가 현재시간을 db에 insert
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # fk를 설정한 변수명에 _id 가 붙게 된다.
    # on_delete = models.CASCADE 삭제 가능하게 할 수 있다
    author = models.ForeignKey(Author,on_delete = models.SET_NULL, null = True)


