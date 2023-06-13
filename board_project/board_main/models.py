from django.db import models

# Create your models here.
# models.py의 class와 DB의 table과 sync를 맞춰 table(column 정보) 자동생성.

# class name 이 table명, 변수는 column명

class Test(models.Model): 
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
