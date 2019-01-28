from django.views.decorators.http import require_http_methods
from referrals.helpers.referral import fetch_specialities


@require_http_methods('GET')
def search_speciality(request):

    user_id = request.user_data['user_id']
    auth_token = request.META.get('HTTP_AUTHORIZATION')
    speciality = request.GET.get('speciality')

    response = fetch_specialities(auth_token, speciality)

    return response