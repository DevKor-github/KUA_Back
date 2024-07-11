from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Course

# http://127.0.0.1:8000/admin/
# Username : postgres, Password : 0514
admin.site.register(Course)
