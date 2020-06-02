from django.urls import path
from django.views.generic.detail import DetailView

from .views import *
from .models import Photo


# 네임스페이스를 지정하기위해 app_name 사용
# app_name을 지정했다면 템플릿 url을 등록할때 photo_를 뺀 나머지 name값을 지정하면 된다.
# <a href="{% url 'photo:photo_upload' %} class="nav-link">Upload</a>
app_name = 'photo'

urlpatterns = [
    # 루트로 요청 : 함수형 뷰 photo_list를 통해 응답, 함수형 뷰 이기 때문에 .as_view() 메서드를 붙이지 않는다.
    path('', photo_list, name='photo_list'),
    # detail/id 로 요청 : DatailView 클래스형 뷰를 통해 응답
    # 사용할 model지정, 템플릿 지정
    path('detail/<int:pk>', DetailView.as_view(model=Photo,
                                               template_name='photo/detail.html'), name='photo_detail'),
    # upload로 요청 : PhotoUploadView로 응답
    path('upload/', PhotoUploadView.as_view(), name='photo_upload'),
    # delete, update 요청 : Pk id 값으로 접속하여 해당 데이터를 수정, 삭제 한다.
    path('delete/<int:pk>', PhotoDeleteView.as_view(), name='photo_delete'),
    path('update/<int:pk>', PhotoUpdateView.as_view(), name='photo_update'),
]
