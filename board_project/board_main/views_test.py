from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
# get 요청 시 html file 그대로 return
def test_html(request):
    return render(request, 'test/test.html')

# get 요청 시 html + data return
def test_html_data(request):
    my_name = "Hwanjin"
    return render(request, 'test/test.html', {'name' : my_name})

# get 요청 시 html + multi data return
def test_html_multi_data(request):
    data = {
        'name': 'Hwanjin',
        'age': 13246418
    }
    return render(request, 'test/test.html', {'data' : data})

# get 요청 시 data만 return
def test_json_data(request):
    data = {
        'name': 'Hwanjin',
        'age': 13246418
    }
    # render라는 의미는 웹개발에서 일반적으로 화면을 return해줄 때 사용하는 용어
    # python의 dict 유사한 json형태로 변환해서 return
    return JsonResponse(data)

# 사용자가 get 요청으로 쿼리파라미터 방식 데이터를 넣어올 때
# 사용자가 get 요청으로 데이터를 넣어오는 방식 2가지
# 1) 쿼리파라미터 방식 : localhost:8000/author?id=10&name=hongildong

def test_html_parameter_data(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    password = request.GET.get('password')
    person = {
        'name' : name,
        'email' : email,
        'password' : password,
    }

    
    return render(request, 'test/test.html', {'data' : person})

# 호출 : http://localhost:8000/parameter_data?id=1&name=hongildong&email=gildon@gmail.com&password=1234

# 2) pathvariable 방식(조금 더 현대적인 방식) : localhost:8000/author/10
def test_html_parameter_data2(request, my_id):
    print(my_id)

    return render(request, 'test/test.html', {})

# 호출 : http://localhost:8000/parameter_data2/10
# terminal에 10 나옴

# form 태그를 활용한 post 방식
# 먼저 화면을 rendering해주는 method
# def test_post_form(request):
#     return render(request, 'test/test_post_form.html')

def test_post_handle(request):
    if request.method == 'post':
        name = request.POST['my_name']
        email = request.POST['my_email']
        password = request.POST['my_password']
        print(name) 
        print(email) 
        print(password)
        return redirect('/') # return HttpResponse('ok') 는 http 응답 시 화면처리 없을 때
    else:
        return render(request, 'test/test_post_form.html')  # 위 함수 하나로 합친 코드      
