from django.views.decorators.http import require_http_methods
# from referrals.helpers.referral import manage_patient_referrals


@require_http_methods('GET')
def manage_provider_referrals(request, patient_id):
    print("yo")