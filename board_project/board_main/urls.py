from django.urls import path
from . import views_test
from django.urls import include
from . import views

urlpatterns = [           
    # path('', views_test.test_html_multi_data),
    # path('test_json', views_test.test_json_data),
    # path('parameter_data', views_test.test_html_parameter_data),
    # path('parameter_data2/<int:my_id>', views_test.test_html_parameter_data2),
    # # path('test_post', views_test.test_post_form),
    # path('test_post_handle', views_test.test_post_handle),
    # path('test_select_one/<int:my_id>', views_test.test_select_one),
    # #호출 http://localhost:8000/test_select_one/1(데이터의 id번호)
    # path('test_select_all', views_test.test_select_all),
    # path('test_select_filter', views_test.test_select_filter),
    # # http://localhost:8000/test_select_filter?name=XXXX
    # path('test_update', views_test.test_update),
    
    path('',views.home),
    path('authors/', views.author_list),
    path('author/new', views.author_new),
    path('author/<int:my_id>', views.author_detail),
    path('author/<int:my_id>/update', views.author_update),
    path('posts/', views.post_list),
    
    

]
