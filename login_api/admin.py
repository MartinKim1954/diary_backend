from django.contrib import admin
from .models import User, Feed

# Register your models here.
admin.site.register(User)
admin.site.register(Feed)