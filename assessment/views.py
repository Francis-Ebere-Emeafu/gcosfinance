from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import FormView
from . import constants
from assessment.forms import BaseApplicationForm
from assessment.models import JobApplication

def get_job_application_from_hash(session_hash):
    # Find and return a not-yet-completed JobApplication
    # with a matching session_hash, or None if no such object exists
    return JobApplication.objects.filter(
    session_hash=session_hash,
    ).exclude(stage=constants.COMPLETE).first()


class JobApplicationView(FormView):
    template_name = 'job_application/job_application.html'
    job_application = None
    form_class = None

    def dispatch(self, request, *args, **kwargs):
        session_hash = request.session.get("session_hash", None)
        # Get the job application for this session. It could be None.
        self.job_application = get_job_application_from_hash(session_hash)
        # Attach the reqeust to "self" so "form_valid()" can access it below.
        self.request =request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # This data is valid, so set this form's session hash in the session.
        self.request.session["session_hash"] = form.instance.session_hash
        current_stage = form.cleaned_data.get("stage")
        # Get the next stage after this one.
        new_stage = constant.STAGE_ORDER[constants.STAGE_ORDER.index(current_stage)+1]
        form.instance.stage = new_stage
        form.save() # This will save the underlying instance.
        if new_stage == constant.COMPLETE:
            return redirect(reverse("job_application:thank_you"))
        # else
        return redirect(reverse("job_application:job_application"))

    def get_form_class(self):
        # if we found a job application that matches the session hash,
        # look at its "stage attribute to decide which stage of the apllication
        # we're on. Otherwise assume we're on stage 1.
        stage = self.job_application.stage if self.job_application else constant.STAGE_1
        # Get the form fields appropriate to that stage
        fields = JobApplication.get_field_by_stage(stage)
        # Use those fields to dynamically create a form with "modelform_factory"
        return modelform_factory(JobApplication, BaseApplicationForm, fields)

    def get_form_kwargs(self):
        # Make sure Django uses the same JobApplication instance we've already
        # been working on
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.job_application
        return kwargs
