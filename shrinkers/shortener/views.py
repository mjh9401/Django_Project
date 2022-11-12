from django.shortcuts import render,redirect
from shortener.models import Users
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

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

@csrf_exempt
def get_user(request,user_id):
    if request.method == 'GET':
        abc = request.GET.get("abc")
        xyz = request.GET.get("xyz")
        user = Users.objects.filter(pk=user_id).first()
        return render(request,"base.html",{"user":user, "params":[abc,xyz]})
    elif request.method == "POST":
        username = request.GET.get("username")
        if username :
            user = Users.objects.filter(pk=user_id).update(username=username)
        return JsonResponse(status=201, data = dict(msg="You just reached with Post Method!"), safe=False)