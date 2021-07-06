import hashlib, random, sys
from django.db import models
from django.utils import timezone

from django.urls import reverse
from django.utils.text import slugify
from account.models import Account


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)

    # objects = QuestionCategoryManager()

    def __str__(self):
        return self.name

    def get_url(self):
        return f"/category/{self.id}"

    def get_number(self):
        # this method returns a number of related questions
        c = Category.objects.annotate(num_questions=models.Count('question')).filter(id=self.id)
        return c[0].num_questions

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name) + str(self.id)
    #     super(Category, self).save(*args, **kwargs)


class Question(models.Model):
    TYPES = (
        (1, 'radio'),
        (2, 'text'),
        )
    text = models.TextField(blank=False, null=False)
    type = models.IntegerField(choices=TYPES, default=1)
    # author = models.ForeignKey(Account, null=True, on_delete=models.SET(value='Deleted'))
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    added_at = models.DateField(auto_now=True)


    objects = QuestionManager()

    def __str__(self):
        return self.text

    def get_url(self):
        return reverse('question', kwargs={'qn_id': self.id})


class QuestionOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    weight = models.IntegerField(default=1)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.text}"

    class Meta:
        ordering = ['weight']


class Answer(models.Model):
    account = models.ForeignKey(Account, on_delete=models.SET(value='Deleted'))
    option = models.ForeignKey(QuestionOption, null=True, on_delete=models.SET_NULL)
    text = models.TextField(null=True)
    active = models.BooleanField(default=True)  # added in case i'll need to deactivate some answers fsr
    added_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.text

    @property
    def question(self):
        return self.option.question


STATUS_CHOICES = (
    (1, 'radio'),
    (2, 'text'),
)


class Project(models.Model):
    description = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    # owner = models.ForeignKey(staff, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.description


class Update(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    notes = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateTimeField(default=timezone.now, editable=False)
    added_by = models.CharField(max_length=35, blank=True)

    def __str__(self):
        return self.notes


















































#
# def create_session_hash():
#     hash = hashlib.sha1()
#     hash.update(str(random.randint(0, sys.maxsize)).encode('utf-8'))
#     return hash.hexdigest()
#
#
# class Assessment(models.Model):
#     # Operational
#     sessioin_hash = models.CharField(max_length=40, unique=True)
#     stage = models.CharField(max_length=10, defualt=constant.STAGE_1)
#     # stage 1 fields
#     first_name = models.CharField(max_length=100, blank=True)
#     last_name = models.CharField(max_length=100, blank=True)
#     email = models.CharField(max_length=100, blank=True)
#     # stage 2 fields
#     phone = models.CharField(max_length=100, blank=True)
#     state = models.CharField(max_length=100, blank=True)
#     address = models.TextField(max_length=100, blank=True)
#     spouse_name = models.CharField(max_length=100, blank=True)
#     spouse_age = models.CharField(max_length=20, blank=True)
#     num_of_children = models.CharField(max_length=20, blank=True)
#
#     budgeting = models.BooleanField(default=False)
#     cash_flow = models.BooleanField(default=False)
#     emergency_funds = models.BooleanField(default=False)
#     life_insurance = models.BooleanField(default=False)
#     retiring_properly = models.BooleanField(default=False)
#     estate_planning = models.BooleanField(default=False) # Will, Trust, Etc
#     debt_management = models.BooleanField(default=False)
#
#     professional_review = models.BooleanField(default=False) # Choice 1. First Time, 2. 1 - 3 years, 3. 3 - 5 years, 4. 5+ years
#     monthly_budget = models.BooleanField(default=False) # Choice 1. yes, 2. No, 3. Need one
#     post_tax_income = models.CharField(max_length=100, blank=True)
#     monthly_expenses = models.CharField(max_length=100, blank=True)
#     emergency_fund = models.CharField(max_length=100)
#
#
#     # stage 3 fields
#     all_is_accurate = models.BooleanField(default=False)
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if not self.session_hash:
#             while True:
#                 session_hash = create_session_hash()
#                 if JobApplication.objects.filter(session_hash=session_hash).count() == 0:
#                     self.session_hash = session_hash
#                     break
#
#     @staticmethod
#     def get_field_by_stage(stage):
#         fields = ['stage'] # Must always be present
#         if stage == constant.STAGE_1:
#             fields.extend(['first_name', 'last_name'])
#         elif stage == constant.STAGE_2:
#             fields.extend(['prior_experience'])
#         elif stage == constant.STAGE_3:
#             fields.extend(['all_is_accurate'])
#         return fields
