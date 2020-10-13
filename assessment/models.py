import hashlib, random, sys
from django.db import models
from . import constants


def create_session_hash():
    hash = hashlib.sha1()
    hash.update(str(random.randint(0, sys.maxsize)).encode('utf-8'))
    return hash.hexdigest()


class Assessment(models.Model):
    # Operational
    sessioin_hash = models.CharField(max_length=40, unique=True)
    stage = models.CharField(max_length=10, defualt=constant.STAGE_1)
    # stage 1 fields
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    # stage 2 fields
    phone = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    address = models.TextField(max_length=100, blank=True)
    spouse_name = models.CharField(max_length=100, blank=True)
    spouse_age = models.CharField(max_length=20, blank=True)
    num_of_children = models.CharField(max_length=20, blank=True)

    budgeting = models.BooleanField(default=False)
    cash_flow = models.BooleanField(default=False)
    emergency_funds = models.BooleanField(default=False)
    life_insurance = models.BooleanField(default=False)
    retiring_properly = models.BooleanField(default=False)
    estate_planning = models.BooleanField(default=False) # Will, Trust, Etc
    debt_management = models.BooleanField(default=False)

    professional_review = models.BooleanField(default=False) # Choice 1. First Time, 2. 1 - 3 years, 3. 3 - 5 years, 4. 5+ years
    monthly_budget = models.BooleanField(default=False) # Choice 1. yes, 2. No, 3. Need one
    post_tax_income = models.CharField(max_length=100, blank=True)
    monthly_expenses = models.CharField(max_length=100, blank=True)
    emergency_fund = models.CharField(max_length=100)
    

    # stage 3 fields
    all_is_accurate = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.session_hash:
            while True:
                session_hash = create_session_hash()
                if JobApplication.objects.filter(session_hash=session_hash).count() == 0:
                    self.session_hash = session_hash
                    break

    @staticmethod
    def get_field_by_stage(stage):
        fields = ['stage'] # Must always be present
        if stage == constant.STAGE_1:
            fields.extend(['first_name', 'last_name'])
        elif stage == constant.STAGE_2:
            fields.extend(['prior_experience'])
        elif stage == constant.STAGE_3:
            fields.extend(['all_is_accurate'])
        return fields

























# Create your models here.
