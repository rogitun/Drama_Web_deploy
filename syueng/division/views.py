from django.shortcuts import redirect, render
from .models import Team
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .forms import CustomTeamForm,CustomUserForm, MessageForm
from .utils import *
# Create your views here.
def home(request):
    teams = Team.objects.all()
    teams,page_range = paginateTeam(request,teams,2)
    
    return render(request,'div_main.html',{'teams':teams,'page_range':page_range})

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
    post = team.post_set.all()
    post,page_range = paginateTeam(request,post,2)
    context = {'team':team,'post':post,'page_range':page_range}
    return render(request,'div_account.html',context)

def profileView(request,pk):
    profile = Team.objects.get(id=pk)
    post = profile.post_set.all()
    post,page_range = paginateTeam(request,post,4)

    context = {'profile':profile,'post':post,'page_range':page_range}
    return render(request,'div_profile.html',context)

def msgBox(request):
    team = request.user.team
    msg_snd = team.sender.all()
    msg_rcv = team.receiver.all()
    snd_count = msg_rcv.filter(is_read=False).count()


    context = {'msg_snd':msg_snd,'msg_rcv':msg_rcv,'snd_count':snd_count}
    return render(request,'message_box.html',context)

def sendView(request,pk):
    team = request.user.team
    msg_snd = team.sender.get(id=pk)
    
    context = {'msg':msg_snd}
    return render(request,'message_view.html',context)

def recvView(request,pk):
    team = request.user.team
    msg_rcv = team.receiver.get(id=pk)

    if msg_rcv.is_read == False:
        msg_rcv.is_read = True
        msg_rcv.save()

    context = {'msg':msg_rcv}
    return render(request,'message_view.html',context)

def msgSend(request,pk):
    whom = Team.objects.get(id=pk)
    who = request.user.team
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = who
            msg.receiver = whom
            msg.name = who.captain
            msg.save()
            return redirect('profile',whom.id)

    context = {'form':form}
    return render(request,'message_send.html',context)