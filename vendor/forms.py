from django import forms

class RFPForm(forms.Form):
    vertical = forms.CharField(max_length=50)
    company = forms.CharField(max_length=250)
    location = forms.CharField(max_length=250)
    name_executive = forms.CharField(max_length=250)
    phone = forms.IntegerField()
    project_name = forms.CharField(max_length=250)
    executive_designation = forms.CharField(max_length=250)
    deal_portfolio = forms.CharField(max_length=1000)
    business_unit = forms.CharField(max_length=250)
    budget_allocated = forms.IntegerField()
    preferred_service_partners = forms.CharField(max_length=1000)
    introduction = forms.CharField(max_length=2000)
    project_goals = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here!'
    )
    selection_schedule = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here!'
    )
    timeline_of_project = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here!'
    )
    elements_of_proposal = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here!'
    )
    evaluation_criteria = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here!'
    )
    possible_roadblocks = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here!'
    )

    def clean(self):
        cleaned_data = super(RFPForm, self).clean()
        vertical = cleaned_data.get('vertical')
        company = cleaned_data.get('company')
        location = cleaned_data.get('location')
        name_executive = cleaned_data.get('name_executive')
        phone = cleaned_data.get('phone')
        project_name = cleaned_data.get('project_name')
        executive_designation = cleaned_data.get('executive_designation')
        deal_portfolio = cleaned_data.get('deal_portfolio')
        business_unit = cleaned_data.get('business_unit')
        budget_allocated = cleaned_data.get('budget_allocated')
        preferred_service_partners = cleaned_data.get('preferred_service_partners')
        introduction = cleaned_data.get('introduction')
        project_goals = cleaned_data.get('project_goals')
        selection_schedule = cleaned_data.get('selection_schedule')
        timeline_of_project = cleaned_data.get('timeline_of_project')
        elements_of_proposal = cleaned_data.get('elements_of_proposal')
        evaluation_criteria = cleaned_data.get('evaluation_criteria')
        possible_roadblocks = cleaned_data.get('possible_roadblocks')
        if not company and not location and not name_executive:
            raise forms.ValidationError('You have to write something!')