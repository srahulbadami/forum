from django.contrib import admin
from .models import User,Forum,Comment


admin.site.register(User)
admin.site.register(Forum)
admin.site.register(Comment)
# Register your models here.
