from django.shortcuts import render
from .models import BloodRequestsModel
from django.views.generic import CreateView
from donors_app.models import DonorDetailsModel


class BloodRequest(CreateView):
    model = BloodRequestsModel
    fields = "__all__"
    template_name = 'blood_requests.html'
    success_url = '/bloodrequest/'


def displayDonors(request):
    res = DonorDetailsModel.objects.all()
    return render(request,"display_donors_state.html",{"data":res})


def selectStateDonors(request):
    state = request.POST.get('donor_state')
    res = DonorDetailsModel.objects.filter(d_state=state)
    return render(request,"display_donor_details.html",{"data":res})


def showDonorDetails(request):
    city = request.POST.get('donor_city')
    bloodgroup = request.POST.get('donor_blood_group')
    res = DonorDetailsModel.objects.filter(d_city=city,d_blood_group=bloodgroup)
    return render(request,"display_donor_details.html",{"data1":res})