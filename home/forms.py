from django import forms
from django.forms import ModelForm, fields
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    
    class Meta:
        model = Project
        fields = ['Title','Upload_image','Desc','demo_link','Tags']
# '__all__'
        widgets ={
             'Tags': forms.CheckboxSelectMultiple(),
        }
    def __init__(self ,*args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name,fields in self.fields.items():
            fields.widget.attrs.update({'class':'input'})

        # self.fields['Title'].widget.attrs.update({'class':'input'})
        # self.fields['Desc'].widget.attrs.update({'class':'input'}) 
        # self.fields['demo_link'].widget.attrs.update({'class':'input'})
           