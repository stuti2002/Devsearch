from django.contrib import admin
from home.forms import ProjectForm

# Register your models here.
from home.models import Project,Review,Tag
admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)

