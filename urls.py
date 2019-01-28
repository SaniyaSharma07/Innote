from django.urls import path
from referrals.controllers.patient_referral import manage_patient_referrals
from referrals.controllers.provider_referral import manage_provider_referrals
from referrals.controllers.search_provider import search_provider
from referrals.controllers.speciality_search import search_speciality

app_name = 'referral'

urlpatterns = [
    path('patients/<patient_id>/referrals', manage_patient_referrals, name='manage_patient_referrals'),
    #list of provider referrals
    path('providers/<referring_provider_id>/referrals', manage_provider_referrals, name='manage_provider_referrals'),
    # search provider using filters like name, speciality
    path('providers/_search', search_provider, name='search_provider'),
    # search specialities(list of specialities)
    path('speciality/_search', search_speciality, name='search_speciality')
]
