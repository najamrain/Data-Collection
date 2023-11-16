from django.shortcuts import render, redirect, get_object_or_404
from .models import Company, Project, Photo
from .forms import CompanyForm, ProjectForm, PhotoForm
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse
from django.urls import reverse_lazy





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


def projects_by_company(request,company_id):
    companies = Company.objects.all()
    print(companies)
    company = Company.objects.get(id=company_id)
    projects = Project.objects.filter(company=company)
    context = {
        'company': company,
        'projects': projects,
        'companies': companies,
    }
    return render(request, 'app/projects_by_company.html',context)





def create_project(request, company_id):
    companies = Company.objects.all()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            company = Company.objects.get(pk=company_id)  # Fetch the company based on the company_id
            form.instance.company = company  # Set the company in the form
            form.save()
            return redirect('projects_by_company', company_id=company_id)  # Redirect to company-specific projects
    else:
        # Preselect the company based on the company_id from the URL
        initial_data = {'company': company_id}
        form = ProjectForm(initial=initial_data)

    context = {'form': form, 'companies': companies}
    return render(request, 'app/project_form.html', context)




def upload_photo(request, company_id, project_id):
    companies = Company.objects.all()
    project = Project.objects.get(pk=project_id)

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            # Set the project based on the project_id from the URL
            form.instance.project = project
            form.save()
            return redirect('project_detail',project_id=project_id)  # Redirect to project detail
    else:
        # Preselect the company based on the company_id from the URL
        form = PhotoForm(initial={'project': project_id})

    context = {'form': form, 'companies': companies}
    return render(request, 'app/photo_upload.html', context)



class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'app/project_update_form.html'

    def get_success_url(self):
        project_id = self.object.id
        return reverse('project_detail', kwargs={'project_id': project_id})






class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'app/project_confirm_delete.html'

    def get_success_url(self):
        # Get the company ID associated with the deleted project
        company_id = self.object.company.id
        project = self.get_object()
        photos = Photo.objects.filter(project=project)

        for photo in photos:
            photo.image.delete()
        photos.delete()

        # Redirect to the company page after project deletion
        return reverse_lazy('projects_by_company', kwargs={'company_id': company_id})

        
    





class PhotoUpdateView(UpdateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'app/photo_update_form.html'
   
    def get_success_url(self):
        project_id = self.object.project.id
        return reverse('project_detail', kwargs={'project_id': project_id})




class PhotoDeleteView(DeleteView):
    model = Photo
    template_name = 'app/photo_confirm_delete.html'

    def get_success_url(self):
        project_id = self.object.project.id
        return reverse('project_detail', kwargs={'project_id': project_id})








