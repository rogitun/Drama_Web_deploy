from django.contrib import admin
from .models import Message, Team
# Register your models here.
admin.site.register(Team)
admin.site.register(Message)