from django.shortcuts import redirect, render
from .models import Team
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .forms import CustomTeamForm,CustomUserForm
# Create your views here.
def home(request):
    teams = Team.objects.all()
    return render(request,'div_main.html',{'teams':teams})

def loginTeam(request):
    message=  ''
    if request.method == 'POST':
        user_id = request.POST['user_id'].lower()
        password = request.POST['password']
        try:#아이디 존재하는지 확인
            user = User.objects.get(username=user_id)
        except:
            message = "존재하지 않는 아이디"
    
        user = authenticate(request,username=user_id,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            message = "로그인 정보 불일치"
    
    return render(request,'loginTeam.html',{'message':message})

def logOut(request):
    logout(request)
    return redirect('login')

def registerTeam(request):
    page = 'register'
    form = CustomUserForm()
    message = ''
    if request.method == 'POST':
        form = CustomUserForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            print('이상함')
            message='필수 정보 미입력'

    context = {'form':form,'page':page,'message':message}
    return render(request,'loginTeam.html',context)

def updateTeam(request,pk):
    team = Team.objects.get(id=pk)

    form = CustomTeamForm(instance=team)

    if request.method == 'POST':
        form = CustomTeamForm(request.POST,request.FILES,instance=team)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form':form}
    return render(request,'edit.html',context)

def accountView(request):
    team = request.user.team

    context = {'team':team}
    return render(request,'div_account.html',context)