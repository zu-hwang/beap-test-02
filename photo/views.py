from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Photo

# Create your views here.


class PhotoUploadView(CreateView):
    model = Photo
    fields = ['photo', 'text']
    # 업로드 할때 사용할 템플릿을 지정한다.
    template_name = 'photo/upload.html'

    # form_valid는 업로드가 끝난 뒤 이동할 페이지를 지정하기 위한 메서드
    def form_valid(self, form):
        # 작성자는 현재 로그인한 유저
        form.instance.author_id = self.request.user.id

        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form': form})


class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'


class PhotoUpdateView(UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'


# request는 함수형뷰의 기본 매개변수
# 함수형 뷰는 클래스 뷰와 달리 모든 기능을 직접 처리해야 한다.


def photo_list(request):
    # Photo 모델의 데이터를 전부 변수에 담는다.
    photos = Photo.objects.all()

    # 포토리스트에 접근했을때 템플릿과 변수에 담을 내용을 전달했다.
    return render(request, 'photo/list.html', {'photos': photos})
