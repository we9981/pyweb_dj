from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
  html = "<h1>Home</h1><p>hello, django!</p>"
  return HttpResponse(html)

def index(request):
  html = "index.html"
  return render(request, html)


def login_action(request):
  if request.method == 'POST':
    username = request.POST.get('u_name', '')
    password = request.POST.get('p_word', '')
    user = auth.authenticate(username=username, password=password)
    #if username == 'admin' and password == 'admin123':
    if user is not None:
      auth.login(request, user) # 登录
      #return render(request, 'event_manage.html', ) #虽然html内容是event_manage，但是URL地址仍然是login_action，而不是event_manage
      #return HttpResponse('login success!') #仅返回字符串，URL地址是login_action
      #return HttpResponseRedirect('/sign/event_manage/') #将URL地址重新定位到event_manage，而不是login_action
      
      #response.set_cookie('user', username, 3600) # 添加浏览器 cookie
      request.session['user'] = username # 将 session 信息记录到浏览器
      response = HttpResponseRedirect('/sign/event_manage/')
      return response
    else:
      return render(request,'index.html', {'error': 'username or password error!'})
  return render(request,'index.html', {'error': 'username or password error!'})

@login_required
def event_manage(request):
  #return render(request,"event_manage.html")
  #username = request.COOKIES.get('user', '') # 读取浏览器 cookie
  username = request.session.get('user', '') 
  return render(request, "event_manage.html", {'user': username})

@login_required
def logout(request):
  auth.logout(request)
  response = HttpResponseRedirect('/sign/index/')
  return response














