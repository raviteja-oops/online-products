from django.contrib import messages
from django.shortcuts import render,redirect
from django.views.generic import CreateView,DetailView
from .models import DonorDetailsModel


class DonorRegistration(CreateView):
    model = DonorDetailsModel
    fields = '__all__'
    template_name = 'donor_registration.html'
    success_url = '/donor_login_registration/'




def donorLoginCheck(request):
    d_username = request.POST.get('dusername')
    d_password = request.POST.get('dpassword')
    try:
        res = DonorDetailsModel.objects.get(d_userid=d_username,d_password=d_password)
    except DonorDetailsModel.DoesNotExist:
        return redirect('donor_login_registration')
    return render(request,"donor_details.html",{"result":res})

def modifyDonorDetails(request):
    modified_username = request.GET.get("modified_userid")
    res = DonorDetailsModel.objects.get(d_userid=modified_username)
    return render(request,"donor_details.html",{"data":res})


def updateDonor(request):
    modified_username = request.POST.get("md_userid")
    modified_email = request.POST.get("md_email")
    modified_contact = request.POST.get("md_contact")
    modified_weight = request.POST.get("md_weight")
    modified_last_donation_date = request.POST.get("md_last_donation_date")
    DonorDetailsModel.objects.filter(d_userid=modified_username).update(d_email=modified_email,d_contact=modified_contact,d_weight=modified_weight,d_last_donation_date=modified_last_donation_date)
    return render(request,"donor_details.html",{"message":"Details Updated Successfully"})


def deleteDonorConfirmation(request):
    return render(request,'donor_details.html',{"delete":True})


def deleteDonor(request):
    delete_d_userid = request.POST.get("delete_userid")
    delete_d_password = request.POST.get("delete_password")
    DonorDetailsModel.objects.filter(d_userid=delete_d_userid,d_password=delete_d_password).delete()
    return render(request,"homepage.html",{"delete_message":"Donor Deleted Successfully"})


def donorLogout(request):
    return redirect('donor_login_registration')