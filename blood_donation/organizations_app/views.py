from django.shortcuts import render


def writeOrganizationDetails(request):
    return render(request,'write_organization_details.html')