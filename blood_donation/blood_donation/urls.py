"""blood_donation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import urls as auth
from django.contrib.auth.views import LoginView
from django.urls import path
from django.views.generic import TemplateView,ListView,DetailView
from homepage_app.models import BloodRequestsModel

from homepage_app import views as homepage_app
from donors_app import views as donors_app
from organizations_app import views as organization_app


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='homepage.html'),name='homepage'),

    # homepage_app URLs

    path('bloodrequest/',homepage_app.BloodRequest.as_view(),name='bloodrequest'),
    path('display_donors/',homepage_app.displayDonors,name='display_donors'),
    path('select_state/',homepage_app.selectStateDonors,name='select_state'),
    path('show_donor_details/',homepage_app.showDonorDetails,name='show_donor_details'),

    # Admin_app URLs

    path('loginpage', LoginView.as_view(template_name="admin_login.html"), name='loginpage'),
    path('login/',TemplateView.as_view(template_name="admin.html"),name='login'),
    path('showrequests/',ListView.as_view(model=BloodRequestsModel,template_name='admin.html'),name='showrequests'),

    #Donors_app URLs

    path('donor_login_registration/',TemplateView.as_view(template_name='donor_homepage.html'),name='donor_login_registration'),
    path('donor_registration/',donors_app.DonorRegistration.as_view(),name='donor_registration'),
    path('donorlogin/',donors_app.donorLoginCheck,name='donorlogin'),
    path('modify_donor_details/',donors_app.modifyDonorDetails,name='modify_donor_details'),
    path('update_donor/',donors_app.updateDonor,name='update_donor'),
    path('delete_donor_confirmation/',donors_app.deleteDonorConfirmation,name='delete_donor_confirmation'),
    path('delete_donor/',donors_app.deleteDonor,name='delete_donor'),
    path('donor_logout/',donors_app.donorLogout,name='donor_logout'),

    #organizations_app URLs

    path('write_organization_details/',organization_app.writeOrganizationDetails,name='write_organization_details')
]
