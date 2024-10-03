from django.shortcuts import render,redirect,get_object_or_404
from .models import Announcement, Department, Doctor,Registration,Emailreceive, User
from . import models
from .forms import RegistrationForm,LoginForm,UserRegistrationForm
from . import forms
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.http import HttpResponse,JsonResponse, Http404
import random
from django.contrib import messages
from django.contrib.sessions.models import Session
# Create your views here.

#首頁
def index(request):
    doctors = Doctor.objects.all()
    doc = []
    for d in doctors:
        doc.append(d)
    doctors = random.sample(doc,k=4)
    if 'username' in request.session:
        username = request.session['username']
    return render(request,'index.html',locals())

#預約掛號
def appointment(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            date = request.POST['date']
            department = request.POST['department']
        except:
            name = None
            message = '請確認每個欄位皆有填入'
        if name != None:
            appointment = models.Appointment.objects.create(name=name, email=email,phone_number=phone, date=date,department = department)
            appointment.save()
            messages.success(request, '信件已寄出！感謝您的來信！')

    return render(request,'appointment.html',locals())

#聯絡我們
def post(request):
    try:
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        m = request.POST['message']
    except:
        name = None
        m = None
        message = '請確認每個欄位皆有填入'
    if m != None:
        post = Emailreceive.objects.create(name=name, email=email,subject=subject, message=m)
        post.save()
        message = '信件已寄出！感謝您的來信！'
    return render(request,'post.html',locals())

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            birthday = form.cleaned_data['birthday']
            gender = form.cleaned_data['gender']
            id_number = form.cleaned_data['id_number']
            phone_number = form.cleaned_data['phone_number']
            date = request.POST['date']
            department = request.POST['department']

            registration = Registration(
                name=name,
                birthday=birthday,
                gender=gender,
                id_number=id_number,
                phone_number=phone_number,
                date = date,
                department = department

            )
            registration.save()
            return redirect('/index')
    else:
        form = RegistrationForm()


    return render(request, 'r.html', locals())

def registered_view(request):
    registrations = Registration.objects.all()
    context = {'registrations': registrations}
    return render(request, 'registered.html', context)

def delete_registration(request, registration_id, superior):
    if request.method == 'DELETE':
        try:
            registration = get_object_or_404(Registration, id=registration_id)
            
            # 获取当前用户对象
            username = request.session['username']
            user = User.objects.get(name = username)
            superior = user.superior
            # 检查用户是否具有删除权限
            if superior is True:
                registration.delete()
                messages.success(request, '成功刪除掛號資訊')
                return JsonResponse({'message': '刪除成功'})  # 返回成功消息
            else:
                messages.error(request, '您沒有權限刪除掛號資訊')
                return JsonResponse({'error': '權限不足'}, status=403)  # 返回权限错误消息

        except Registration.DoesNotExist:
            return JsonResponse({'error': '掛號資料不存在'}, status=404)
    else:
        return JsonResponse({'error': '請求無效'}, status=400)

#醫生群介紹
def inner_page(request):
    doctors = Doctor.objects.all()
    return render(request,'inner-page.html',locals())

def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            checkname = request.POST['username'].strip()
            checkpassword = request.POST['password']
            try:
                user = User.objects.get(name=checkname)
                if user.password == checkpassword:
                    request.session['username'] = checkname
                    request.session['password'] = checkpassword
                    messages.add_message(request,messages.SUCCESS,'登入成功') 
                    request.session.set_expiry(0) #瀏覽企關閉session失效
                    return redirect('/index')
                else:
                    messages.add_message(request,messages.WARNING,'密碼錯誤，請再輸入一次')
            except models.User.DoesNotExist:
                 messages.add_message(request,messages.WARNING,'找不到使用者') 

        else:
            messages.add_message(request,messages.INFO,'請檢查輸入欄位')
    
    else:
        login_form = LoginForm()
    
    return render(request, 'login.html', locals())


def logout(request):
    if 'username' in request.session:
        request.session.flush()  # 清空当前用户的会话数据
        
    return redirect('/')  

    

#使用者註冊
def user_registration(request):
    if request.method == 'POST':
        register_form = forms.UserRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, '註冊成功')
            return redirect('/index')
        else:
            messages.error(request, '請檢查欄位')
    else:
        register_form = forms.UserRegistrationForm()
    return render(request,'register.html',locals())

#show掛號
def show_r(request):
    # if 'username' not in request.session:
    #     return redirect('/index')
    # try:
    #     registrations = models.Registration.objects.all()
    # except:
    #     message = '目前尚無掛號'
    registrations = Registration.objects.all()
    return render(request,'show_registration.html',locals())

# 個人資料
def profile(request):
    if 'username' in request.session:
        username = request.session['username']
        try:
            profiles = User.objects.get(name=username)  # 假设你使用的是用户名来查询用户信息
            # 如果是自定义用户模型，可能是 User.objects.get(name=username)，根据实际情况调整

        except User.DoesNotExist:
            return redirect('/login/')  # 用户不存在，重定向到登录页面或其他逻辑处理
    else:
        return redirect('/login/')  # 没有用户名在 session 中，重定向到登录页面或其他逻辑处理


    return render(request, 'profile.html', locals())  # 渲染个人资料页面，并传递用户对象到模板中




