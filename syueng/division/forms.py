from django.contrib.auth.forms import UserCreationForm
from django.forms.models import ModelForm
from .models import *
from django.contrib.auth.models import User

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        labels ={
            'username':'아이디',
            'first_name':'팀명',
            'last_name':'팀장',
            'email':'이메일',
        }
    
    def __init__(self,*args,**kwargs):
        super(CustomUserForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class CustomTeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['username','name','captain','short_intro','profile_image']
        labels ={
            'username':'아이디',
            'name':'팀명',
            'captain':'팀장',
            'short_intro':'소개'
        }
    
    def __init__(self,*args,**kwargs):
        super(CustomTeamForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['title','desc']
        labels = {
            'title':'제목',
            'desc':'본문',
        }


    def __init__(self,*args,**kwargs):
        super(MessageForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})