from django.shortcuts import render
from .forms import RegisterFrom

# Create your views here.


def register(request):
    # 회원정보가 POST를 통해 전달되었을때
    if request.method == 'POST':
        # 우리가 만든 forms.py의  RegisterFor을 POST로 받은 값의 유효성 검사를 진행하며 이상이 없으면 DB에 저장한다.
        user_form = RegisterFrom(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = RegisterFrom()
    return render(request, 'registration/register.html', {'form': user_form})
