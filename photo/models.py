from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Photo(models.Model):
    # author 는 User 테이블과 포린키 관계를 둔다. User테이블의 데이터가 삭제될경우 옵션으로 on_delete를 CASCADE로 설정하였다.
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_photos')
    # 업로드 되는 파일은 photos폴더에 년/월/일 하위에 업로드 된다. 이미지가없다면 기본 이미지로 데이터베이스에 저장된다.
    photo = models.ImageField(
        upload_to='photos/%y/%m/%d', default='photos/no_image.png')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # 옵션 클래스인 Meta 클래스를 작성하여 순번옵션을 설정한다.
    class Meta:
        ordering = ['-updated']

    # get_absolute_url은 상세페이지의 주소를 반환하는 메서드를 작성했다.
    def get_absolute_url(self):
        # reverse는 url패턴을 통해 해당 주소를 찾아 이동하게 된다. 즉, urls.py에 작성한 name속성을 찾아가 이동한단말씀!
        # args는 여러값들을 리스트로 전달하는데 사용하는데 여기서는 pk값을 전달하도록 한다.
        return reverse('photo:photo_detail', args=[str(self.id)])

    # __str__은 photo클래스를 설명하는 문자열을 리턴한다.
    def __str__(self):
        return self.author.username+" " + self.created.strftime('%y-%m-%d %H:%M:%S')


#! on_delete의 종류
# CASCADE : 연결된 객체가 지워지면 해당 하위 객체도 같이 삭제된다.
# PROTECT : 말그대로 보호됨, 하위객채가 남아있다면 연결된 객체가 지워지지 않음
# SET_NULL : 연결된 객체만 삭제하고 필드값을 null로 설정한다
# SET_DEFAULT : 연결된 객체만 삭제하고 필드 값을 설정된 기본 값으로 변경
# SET() : 연결된 객채만 삭제하고 인자로 지정된 값으로 변경
# DO_NOTIONG : 아무것도 하지 않음

#! related_name의 역할은?
# 연결된 객체에서 하위객체의 목록을 부를때 사용하는 이름!
