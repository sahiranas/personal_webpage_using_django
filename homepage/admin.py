from django.contrib import admin

# Register your models here.
from . models import Education, PythonProjects, WebProject


admin.site.register(Education)

admin.site.register(PythonProjects)

admin.site.register(WebProject)
