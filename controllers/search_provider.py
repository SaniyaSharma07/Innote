from django.views.decorators.http import require_http_methods
from referrals.helpers.referral import inref_search_provider
from commons.utils.response import OK

@require_http_methods('GET')
def search_provider(request, patient_zipcode):

    if request.method == 'GET':
        user_id = request.user_data['user_id']
        auth_token = request.META.get('HTTP_AUTHORIZATION')
        # view_name = request.url_info['view_name']
        request_id = request.request_id
        speciality = request.GET.get('speciality')
        
        patient_zipcode = request.GET.get('patient_zipcode')
        # is_name = request.GET.get('is_name')
        # referring_provider_name = request.GET.get('name')
        response = inref_search_provider(auth_token, speciality, patient_zipcode)

        return OK(response)