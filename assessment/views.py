from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import FormView
from django.forms import modelformset_factory, BaseFormSet

from assessment.models import Question, Answer, Category, Project
from assessment.forms import QuestionForm, AnswerForm, EditProjectForm, CreateUpdateForm
from account.models import Account
# from .forms import AskForm, AnswerForm, CategoryForm

def questions(request):
    questions = Question.objects.all()
    AnswerFormset = modelformset_factory(Question, extra=0, fields=[], form=AnswerForm)
    formset = AnswerFormset(queryset=questions)
    for qst in questions:
        print(qst)

    if request.method == "POST":
        formset = AnswerFormset(request.POST, queryset=questions)
        if formset.is_valid():
            for form in formset.forms:
                option = form.cleaned_data['answer']
                print(option)
                # Answer.objects.create(
                #     account=request.user,
                #     option=option,
                #     text='',
                # )
            return redirect('home')
    else:
        formset = AnswerFormset(queryset=questions)

    context = {"formset": formset}

    return render(request, 'assessment/questions.html', context)


def projects(request):
    project_formset = modelformset_factory(Project, form=CreateUpdateForm, extra=0)
     # fields=['status']
    projects = Project.objects.all()

    if request.method == 'POST':
        formset = project_formset(request.POST, request.FILES, queryset=projects)
        if formset.is_valid():
            for f in formset:
                project = f.save(commit = False)

                update_form = CreateUpdateForm(request.POST,request.FILES)
                if update_form.is_valid():
                    update = update_form.save(commit = False)
                    update.project = project
                    project.save()
                    update.save()
                else:
                    print(update_form.errors)
            return redirect('/')
        else:
            print(formset.errors)
    else:
        formset = project_formset(queryset=projects)
        update_form = CreateUpdateForm()
        return render(request,'assessment/projects.html',{'formset':formset, 'update_form':update_form})












































# from . import constants
# from assessment.forms import BaseApplicationForm
# from assessment.models import JobApplication
#
# def get_job_application_from_hash(session_hash):
#     # Find and return a not-yet-completed JobApplication
#     # with a matching session_hash, or None if no such object exists
#     return JobApplication.objects.filter(
#     session_hash=session_hash,
#     ).exclude(stage=constants.COMPLETE).first()
#
#
# class JobApplicationView(FormView):
#     template_name = 'job_application/job_application.html'
#     job_application = None
#     form_class = None
#
#     def dispatch(self, request, *args, **kwargs):
#         session_hash = request.session.get("session_hash", None)
#         # Get the job application for this session. It could be None.
#         self.job_application = get_job_application_from_hash(session_hash)
#         # Attach the reqeust to "self" so "form_valid()" can access it below.
#         self.request =request
#         return super().dispatch(request, *args, **kwargs)
#
#     def form_valid(self, form):
#         # This data is valid, so set this form's session hash in the session.
#         self.request.session["session_hash"] = form.instance.session_hash
#         current_stage = form.cleaned_data.get("stage")
#         # Get the next stage after this one.
#         new_stage = constant.STAGE_ORDER[constants.STAGE_ORDER.index(current_stage)+1]
#         form.instance.stage = new_stage
#         form.save() # This will save the underlying instance.
#         if new_stage == constant.COMPLETE:
#             return redirect(reverse("job_application:thank_you"))
#         # else
#         return redirect(reverse("job_application:job_application"))
#
#     def get_form_class(self):
#         # if we found a job application that matches the session hash,
#         # look at its "stage attribute to decide which stage of the apllication
#         # we're on. Otherwise assume we're on stage 1.
#         stage = self.job_application.stage if self.job_application else constant.STAGE_1
#         # Get the form fields appropriate to that stage
#         fields = JobApplication.get_field_by_stage(stage)
#         # Use those fields to dynamically create a form with "modelform_factory"
#         return modelform_factory(JobApplication, BaseApplicationForm, fields)
#
#     def get_form_kwargs(self):
#         # Make sure Django uses the same JobApplication instance we've already
#         # been working on
#         kwargs = super().get_form_kwargs()
#         kwargs["instance"] = self.job_application
#         return kwargs
