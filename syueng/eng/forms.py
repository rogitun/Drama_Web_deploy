from django.db.models import fields
from .models import Post, Review
from django.forms.models import ModelForm

class postForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','date','image','paid','desc']
    
    def __init__(self,*args,**kwargs):
        super(postForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class CustomReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['desc']

    def __init__(self,*args,**kwargs):
        super(CustomReviewForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
