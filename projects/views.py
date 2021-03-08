from django.shortcuts import render, redirect

# Create your views here.
from django.views import generic
from projects.forms import CredentialsForm
from django.urls import reverse_lazy
from custom_script.jira_module import JiraModule
from projects.models import Projects, UserCredentials
from django.http import  HttpResponseRedirect



class CredentialsListView(generic.ListView):
    model = UserCredentials
    template_name = 'list.html'


class DeleteCredentialView(generic.View):
    model = UserCredentials
    success_url = reverse_lazy('projects:list_credentials')

    def get(self, request, credential_id, *args, **kwargs):
        self.model.objects.get(pk=credential_id).delete()
        return HttpResponseRedirect(self.success_url)


class ProjectView(generic.View):

    credential_form_class = CredentialsForm
    initial = {'key': 'value'}
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        form = self.credential_form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    @staticmethod
    def get_projects(form):
        data = form.cleaned_data
        jira = JiraModule(data["username"], data["password"], data["end_point"])

        return jira.get_jira_projects()

    @staticmethod
    def save_selected_project(selected_projects, credentials_obj):
        project_bulk = [Projects(credentials=credentials_obj,
                                 project_id=project["id"],
                                 key=project["key"],
                                 name=project["name"]) for project in selected_projects]
        Projects.objects.bulk_create(project_bulk)

    def post(self, request, *args, **kwargs):
        data = None
        post_data = {**request.POST}
        save_mode = False
        if "save" in post_data:
            save_mode = True
            selected_projects = post_data.pop('selected_projects')
            post_data.pop('save')

        form = self.credential_form_class(request.POST)
        if form.is_valid():
            data = self.get_projects(form)

        if save_mode:
            selected_projects = [{**project} for project in data if project["id"] in selected_projects]
            self.save_selected_project(selected_projects, form.save())
            return render(request, self.template_name, {'form': form, 'msg': "Successfully Saved!!"})
        return render(request, self.template_name, {'form': form, 'data': data, 'fetch': True})

