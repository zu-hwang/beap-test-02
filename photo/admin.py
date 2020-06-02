from django.contrib import admin
from .models import Photo

# Register your models here.


class PhotoAdmin(admin.ModelAdmin):
    # 관리자페이지 데이터테이블 보기 좋게 커스텀 하자
    # 테이블의 컬럼명을 작성하여 표 머리를 지정한다.
    list_display = ['id', 'author', 'created', 'updated']
    # 포린키필드의 경우 연결된모델의 객체목록을 출력하고 선택해야하는데 목록이 너무 길 경우 불편해진다. 이런경우 raw_id_fields로 설정하면 값을 써넣는 형태로 바뀌고 검색기능을 사용해 선택할 수 있게 된다.
    raw_id_fields = ['author']
    # 필터기능을 사용할 필드를 선택한다. 장고가 적절하게 필터범위를 출력해준다.
    list_filter = ['created', 'updated', 'author']
    # 검색기능을 통해 검색할 필드를 설정한다. 주의 : 포린키 필드는 설정할 수 없다
    search_fields = ['test', 'created']
    # 관리자 사이트에서 기본 정렬을 설정한다.(모델에서 작성한 오더링과 관련 없다.)
    ordering = ['-updated', '-created']


admin.site.register(Photo, PhotoAdmin)
