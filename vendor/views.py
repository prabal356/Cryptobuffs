from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import vendor, RFT, RFP
from django.template import loader
from django.http import Http404
# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import RFPForm


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def index(request, x = None):
    all_vendors = RFP.objects.all()
    context = {'all_vendors':all_vendors}
    return render(request, "home.html", context)


def vendor_homepage(request):
    all_rfts = RFT.objects.all()
    context = {'all_rfts' : all_rfts}
    return render(request, "vendor/index_rft.html", context)


def detail(request, vendor_id):
    try:
        buyer_1 = RFP.objects.get(pk = vendor_id)
    except vendor.DoesNotExist:
        raise Http404("Vendor Does not exist")
    return render(request, "vendor/rfp_obj.html", {"vendor_1":buyer_1})


def vendor_details(requests, vendor_id_1):
    try:
        vendor_1 = RFP.objects.get(pk = vendor_id_1)
    except RFP.DoesNotExist:
        raise Http404("Vendor Does not exist")
    return render(requests, "vendor/rfp_obj.html", {"vendor_1":vendor_1})


def rft_details(requests, rft_id):
    try:
        rft_1 = RFT.objects.get(pk = rft_id)
    except RFT.DoesNotExist:
        raise Http404("Vendor Does not exist")
    return render(requests, "vendor/rft_object.html", {"rft_1":rft_1})


def create_rfp(request):
        if request.method == 'POST':
            post = RFP(data = request.POST)
            print(request.POST.get('vertical'))
            post.vertical = request.POST.get('vertical')
            post.company = request.POST.get('company')
            post.location = request.POST.get('location')
            post.name_executive = request.POST.get('name_executive')
            post.phone = request.POST.get('phone')
            post.project_name = request.POST.get('project_name')
            post.executive_designation = request.POST.get('executive_designation')
            post.deal_portfolio = request.POST.get('deal_portfolio')
            post.business_unit = request.POST.get('business_unit')
            post.budget_allocated = request.POST.get('budget_allocated')
            post.preferred_service_partners = request.POST.get('preferred_service_partners')
            post.introduction = request.POST.get('introduction')
            post.project_goals = request.POST.get('project_goals')
            post.selection_schedule = request.POST.get('selection_schedule')
            post.timeline_of_project = request.POST.get('timeline_of_project')
            post.elements_of_proposal = request.POST.get('elements_of_proposal')
            post.evaluation_criteria = request.POST.get('evaluation_criteria')
            post.possible_roadblocks = request.POST.get('possible_roadblocks')
            #post.token_address = request.POST.get("token_address")
            post.save()
            return render(request, 'vendor/rfp_form.html')

        else:
            return render(request, 'vendor/rfp_form.html')



def create_rft(request):
    if request.POST.get("company") and request.POST.get('location') and request.POST.get("name_executive"):
        post = RFT()
        post.vertical = request.POST.get('vertical')
        post.company = request.POST.get('company')
        post.location = request.POST.get('location')
        post.name_executive = request.POST.get('name_executive')
        post.phone = request.POST.get('phone')
        post.project_name = request.POST.get('project_name')
        post.executive_designation = request.POST.get('executive_designation')
        post.deal_portfolio = request.POST.get('deal_portfolio')
        post.business_unit = request.POST.get('business_unit')
        post.budget_allocated = request.POST.get('budget_allocated')
        post.preferred_service_partners = request.POST.get('preferred_service_partners')
        post.introduction = request.POST.get('introduction')
        post.project_goals = request.POST.get('project_goals')
        post.selection_schedule = request.POST.get('selection_schedule')
        post.timeline_of_project = request.POST.get('timeline_of_project')
        post.elements_of_proposal = request.POST.get('elements_of_proposal')
        post.evaluation_criteria = request.POST.get('evaluation_criteria')
        post.possible_roadblocks = request.POST.get('possible_roadblocks')
        #post.token_address = request.POST.get("token_address")
        post.save()
        return render(request, 'vendor/rft_form.html')
    else:
        return render(request, 'vendor/rfp_form.html')

