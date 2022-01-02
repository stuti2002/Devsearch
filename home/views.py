from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from home.forms import ProjectForm
from .models import Project

# Create your views here.
# projectlist=[{
#     'id':'1',
#     'Title':'weather App',
#     'branch':'cse'
#     },
#     {
#      'id':'2',
#      'name':'Portfolio',
#      'branch':'IT'}
# ]

# for main page(all projects)
def singleproject(request):
    # msg='projects'
    # Number=9
    projects=Project.objects.all()
    context={
        # 'msg':msg,'Number':Number,
        'projects':projects
    }
    return render(request,'Projects/singleproject.html',context)



# for viewing single project page
def project(request,pk):
    #projectobj=None
    # for i in projectlist:
    #     if i['id']==pk:
    #         projectobj=i

    projectobj=Project.objects.get(id=pk)
    Tags=projectobj.Tags.all()
    context={'projectobj':projectobj,'tags':Tags}
    
    return render(request,'Projects/project.html',context)
    #{'project':projectobj})


# To create Form page
@login_required(login_url="login")
def CreateProject(request):
    form=ProjectForm()
    if request.method=='POST':
        form=ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('singleproject')
    context={'form':form}
    return render(request, 'Projects/projects_form.html',context)


# To edit project information
@login_required(login_url="login")
def UpdateProject(request,pk):
    
    project=Project.objects.get(id=pk)
    form=ProjectForm(instance=project)
    if request.method=='POST':
        form=ProjectForm(request.POST ,instance=project)
        if form.is_valid():
            form.save()
            return redirect('singleproject')
    context={'form':form}
    return render(request, 'Projects/projects_form.html',context)



# To delete project
@login_required(login_url="login")
def DeleteProject(request,pk):
    project=Project.objects.get(id=pk)
    if request.method=='POST':
        project.delete()
        return redirect('singleproject')
    context={'object':project}
    return render(request,'Projects/Delete_project.html',context)

