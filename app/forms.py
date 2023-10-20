from django import forms
from .models import Company, Project, Photo

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['user_baba', 'company']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['company', 'project_name', 'main_contractor_name', 'plot_area', 'built_up_area', 'location']

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['project', 'image']




# class ProjectForm(forms.ModelForm):
#     class Meta:
#         model = Project
#         fields = ['company', 'project_name', 'main_contractor_name', 'plot_area', 'built_up_area', 'location']

from django import forms
from .models import Project

from django import forms
from .models import Project, Company

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['company', 'project_name', 'main_contractor_name', 'plot_area', 'built_up_area', 'location']
    
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        company_choices = [(company.id, company.company) for company in Company.objects.all()]
        
        self.fields['company'].widget = forms.Select(choices=company_choices)
        self.fields['company'].widget.attrs.update({'placeholder': 'Select a company'})
        self.fields['project_name'].widget.attrs.update({'placeholder': 'Project Name'})
        self.fields['main_contractor_name'].widget.attrs.update({'placeholder': 'Main Contractor Name'})
        self.fields['plot_area'].widget.attrs.update({'placeholder': 'Plot Area'})
        self.fields['built_up_area'].widget.attrs.update({'placeholder': 'Built-Up Area'})
        self.fields['location'].widget.attrs.update({'placeholder': 'Location'})





from .models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['project', 'image']

    def __init__(self, *args, **kwargs):
        super(PhotoForm, self).__init__(*args, **kwargs)
        self.fields['project'].widget = forms.Select(choices=[(project.id, project.project_name) for project in Project.objects.all()])



