from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
dic = {}

def Login(request):
    if request.method == 'GET':
        return render(request, 'Login.html')
    elif request.method == 'POST':
        username1 = request.POST.get('username1')
        password1 = request.POST.get('password1')
        if username1 in dic:
            if dic[username1] == password1:
                return render(request, 'succeed.html')
            else:
                error_msg='账号或密码错误'
                return render(request,'Login.html',{'error_msg':error_msg})
        else:
            error_msg='不存在该账号'
            return render(request, 'Login.html', {'error_msg': error_msg})

def psd(request):
    return render(request, 'psd.html')

def Register(request):
    if request.method == 'GET':
        return render(request, 'Register.html')
    elif request.method == 'POST':
        username2 = request.POST.get('username2')
        password2 = request.POST.get('password2')
        ic = request.POST.get('ic')
        if username2 in dic:
            error_msg = '该账号已存在'
            return render(request, 'Register.html', {'error_msg': error_msg})
        elif len(password2)<6:
            error_msg = '密码长度不够'
            return render(request, 'Register.html', {'error_msg': error_msg})
        elif ic != '7364':
            error_msg = '验证码错误'
            return render(request, 'Register.html', {'error_msg': error_msg})
        elif ic == '7364':
            dic[username2] = password2
            return render(request, 'Login.html')
