from django.db import models

# Create your models here.

class vendor(models.Model):
    name = models.CharField(max_length=250)
    email_id = models.CharField(max_length=250)
    phone = models.IntegerField()
    loginid = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    vendor = models.BooleanField(default = False)
    bidder = models.BooleanField(default = False)
    token_address = models.CharField(max_length=100, default=None)
    def __str__(self):
        return self.name +  "_" + self.loginid + "_isvendor_"+ str(self.vendor)


class RFT(models.Model):
    vertical = models.CharField(max_length=250, default=None, null = True)
    vendor_name = models.CharField(max_length=250, default=None, null = True)
    location = models.CharField(max_length=250, default=None, null = True)
    name_executive = models.CharField(max_length=250, default=None, null = True)
    email_id = models.CharField(max_length=250, default=None, null = True)
    phone = models.IntegerField()
    capability_area = models.CharField(max_length=250, default=None, null = True)
    service_line = models.CharField(max_length=250, default=None, null = True)
    budget_allocated = models.IntegerField()
    preferred_partners = models.CharField(max_length=1000, default=None, null = True)

    deal_portfolio = models.CharField(max_length=1000, default=None, null = True)
    business_unit = models.CharField(max_length=250, default=None, null = True)

    introduction = models.CharField(max_length=2000, default=None, null = True)
    project_goals = models.CharField(max_length=2000, default=None, null = True)
    selection_schedule = models.CharField(max_length=1000, default=None, null = True)
    timeline_of_project = models.CharField(max_length=250, default=None, null = True)
    elements_of_proposal = models.CharField(max_length=2000, default=None, null = True)
    evaluation_criteria = models.CharField(max_length=2000, default=None, null = True)
    possible_roadblocks = models.CharField(max_length=1000, default=None, null = True)


class RFP(models.Model):
    vertical = models.CharField(max_length=250, default=None, null = True)
    company = models.CharField(max_length=250, default=None, null = True)
    location = models.CharField(max_length=250, default=None, null = True)
    name_executive = models.CharField(max_length=250, default=None, null = True)
    phone = models.IntegerField(null = True)
    project_name = models.CharField(max_length=250, default=None, null = True)
    executive_designation = models.CharField(max_length=250, default=None, null = True)
    deal_portfolio = models.CharField(max_length=1000, default=None, null = True)
    business_unit = models.CharField(max_length=250, default=None, null = True)
    budget_allocated = models.IntegerField(null = True)
    preferred_service_partners = models.CharField(max_length=1000, default=None, null = True)
    introduction = models.CharField(max_length=2000, default=None, null = True)
    project_goals = models.CharField(max_length=2000, default=None, null = True)
    selection_schedule = models.CharField(max_length=1000, default=None, null = True)
    timeline_of_project = models.CharField(max_length=250, default=None, null = True)
    elements_of_proposal = models.CharField(max_length=2000, default=None, null = True)
    evaluation_criteria = models.CharField(max_length=2000, default=None, null = True)
    possible_roadblocks = models.CharField(max_length=1000, default=None, null = True)



