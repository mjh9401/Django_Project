from django.shortcuts import render,redirect
from shortener.models import Users

# Create your views here.

def index(request):
    user = Users.objects.filter(username="admin_").first()

    # 장고ORM get은 결과가 무조건 1개밖에 없는 것을 가져온다.
    # get은 유효성 검사에 사용된다.
    # user = Users.objects.get(username="admin_")
    email = user.email if user else "Anonymous User!"
    print(email)
    print(request.user.is_authenticated)
    if request.user.is_authenticated is False:
        email = "Anonymous User!"
    return render(request,"base.html",{"welcome_msg" : f"Hello {email}"})

def redirect_test(request):
    return redirect("index")