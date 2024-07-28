from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
def register(request):
    """注册新⽤户"""
    if request.method != 'POST':
        # 显⽰空的注册表单
        form = UserCreationForm()
    else:
        # 处理填写好的表单
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # 让⽤户⾃动登录，再重定向到主⻚
            login(request, new_user)
            return redirect('learning_logs:index')
    # 显⽰空表单或指出表单⽆效
    context = {'form': form}
    return render(request, 'registration/register.html', context)