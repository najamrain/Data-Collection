from django.shortcuts import render, redirect, get_object_or_404
from .models import Company, Project, Photo
from .forms import CompanyForm, ProjectForm, PhotoForm



def homepage(request):
    companies = Company.objects.all()
    print(companies)

    return render(request, "app/base.html" ,{'companies': companies})

def company_list(request):
    companies = Company.objects.all()
    print(companies)
    return render(request, 'app/company_list.html', {'companies': companies})

def company_detail(request, company_id):
    companies = Company.objects.all()
    print(companies)
    company = get_object_or_404(Company, id=company_id)
    return render(request, 'app/company_detail.html', {'company': company, 'companies': companies})

def project_list(request):
    companies = Company.objects.all()
    print(companies)
    projects = Project.objects.all()
    return render(request, 'app/project_list.html', {'projects': projects, 'companies': companies})

def project_detail(request, project_id):
    companies = Company.objects.all()
    print(companies)
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'app/project_detail.html', {'project': project, 'companies': companies})

def photo_list(request):
    companies = Company.objects.all()
    print(companies)
    photos = Photo.objects.all()
    return render(request, 'app/photo_list.html', {'photos': photos, 'companies': companies})

def photo_detail(request, photo_id):
    companies = Company.objects.all()
    print(companies)
    photo = get_object_or_404(Photo, id=photo_id)
    return render(request, 'app/photo_detail.html', {'photo': photo, 'companies': companies})


def projects_by_company(request, company_id):
    companies = Company.objects.all()
    print(companies)
    company = Company.objects.get(id=company_id)
    projects = Project.objects.filter(company=company)
    context = {
        'company': company,
        'projects': projects,
        'companies': companies
    }
    return render(request, 'app/projects_by_company.html',context)


from .forms import ProjectForm

# def create_project(request):
#     companies = Company.objects.all()
#     if request.method == 'POST':
#         form = ProjectForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('project_list') 
#     else:
#         form = ProjectForm()
    
#     context = {'form': form,'companies':companies }
#     return render(request, 'app/project_form.html', context)

from django.shortcuts import render, redirect
from .forms import ProjectForm

def create_project(request):
    companies = Company.objects.all()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            # Prepopulate the company field with the user's company
            # form.instance.company = request.user.company  # Assuming user has a 'company' attribute

            form.save()
            return redirect('project_list')  # Redirect to the project list or any other desired view
    else:
        # Create a new project form and prepopulate the company field if the user is logged in
        if request.user.is_authenticated and hasattr(request.user, 'company'):
            form = ProjectForm(initial={'company': request.user.company.id})
        else:
            form = ProjectForm()

    context = {'form': form, 'companies':companies}
    return render(request, 'app/project_form.html', context)

from .forms import PhotoForm


def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo_list')  # Redirect to the photo list or any other desired view
    else:
        form = PhotoForm()
    
    context = {'form': form}
    return render(request, 'app/photo_upload.html', context)

from django.views.generic.edit import UpdateView
from .models import Project
from .forms import ProjectForm

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'app/project_update_form.html'
    success_url = '/'  # Replace with the URL where you want to redirect after editing a project


from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Project, Photo

from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Project, Photo

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'app/project_confirm_delete.html'
    success_url = reverse_lazy('project_list')

    def get_success_url(self):
        project = self.get_object()
        # Delete associated photos
        photos = Photo.objects.filter(project=project)
        for photo in photos:
            photo.image.delete()
        photos.delete()
        return self.success_url
    

from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import Photo
from .forms import PhotoForm

class PhotoUpdateView(UpdateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'app/photo_update_form.html'
    success_url = reverse_lazy('photo_list')

from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Photo

class PhotoDeleteView(DeleteView):
    model = Photo
    template_name = 'app/photo_confirm_delete.html'
    success_url = reverse_lazy('photo_list')







